# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pandas",
#   "numpy",
#   "matplotlib",
#   "seaborn",
#   "requests",
#   "scipy",
#   "chardet",
#   "tenacity"
# ]
# ///

import os
import sys
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import zscore
import chardet
import requests
from tenacity import retry, stop_after_attempt, wait_fixed

# Function to load dataset
def load_dataset(file_path):
    try:
        with open(file_path, 'rb') as f:
            encoding = chardet.detect(f.read())['encoding']
        df = pd.read_csv(file_path, encoding=encoding)
        print(f"Loaded dataset: {file_path} ({df.shape[0]} rows, {df.shape[1]} columns).")
        return df
    except Exception as e:
        print(f"Error loading dataset {file_path}: {e}")
        sys.exit(1)

# Function to generate visualizations
def generate_visualizations(df, output_dir):
    sns.set_theme(style="whitegrid")
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()

    if len(numeric_cols) > 1:
        sns.pairplot(df[numeric_cols].dropna())
        pairplot_path = os.path.join(output_dir, "pairplot.png")
        plt.savefig(pairplot_path, dpi=300)
        plt.close()
        print(f"Pairplot saved: {pairplot_path}")

    if "target" in df.columns:
        sns.histplot(df["target"].dropna(), kde=True, bins=30)
        plt.title("Distribution of Target Variable")
        target_dist_path = os.path.join(output_dir, "target_distribution.png")
        plt.savefig(target_dist_path, dpi=300)
        plt.close()
        print(f"Target distribution saved: {target_dist_path}")

# Function to create correlation matrix
def create_correlation_matrix(df, output_dir):
    numeric_cols = df.select_dtypes(include=[np.number])
    if numeric_cols.empty:
        print("No numeric columns available for correlation matrix.")
        return
    corr_matrix = numeric_cols.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    heatmap_path = os.path.join(output_dir, "correlation_matrix.png")
    plt.savefig(heatmap_path, dpi=300)
    plt.close()
    print(f"Correlation matrix saved: {heatmap_path}")

# Retry wrapper for LLM API calls
@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def call_llm(prompt):
    url = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
    
    # Directly using the API key
    AIPROXY_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIyZjMwMDMxNTdAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.jqgA4t_kF3xuPBBPlGeLSKobS64VlLoTFSdh9MUMchQ"  # Replace with your actual API key

    headers = {
        "Authorization": f"Bearer {AIPROXY_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are a data analyst."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 500
    }
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()['choices'][0]['message']['content']

# Function to narrate the analysis
def narrate_analysis(df, visualizations):
    prompt = (
        f"The dataset contains {df.shape[0]} rows and {df.shape[1]} columns. "
        f"Here are the column names and data types: {df.dtypes.to_dict()}. "
        f"Summary statistics: {df.describe(include='all').to_string()}. "
        "Please analyze this data, summarize key insights, and suggest potential actions based on the analysis."
    )
    return call_llm(prompt)

# Function to save README
def save_readme(output_dir, dataset_name, summary, story, visualizations):
    readme_path = os.path.join(output_dir, "README.md")
    with open(readme_path, "w") as f:
        f.write(f"# Analysis of {dataset_name}\n\n")
        f.write("## Summary\n")
        f.write(f"```\n{summary}\n```\n\n")
        f.write("## Narrative\n")
        f.write(f"{story}\n\n")
        for viz in visualizations:
            f.write(f"![{viz}]({viz})\n")
    print(f"README saved: {readme_path}")

# Main function
def main():
    if len(sys.argv) != 2:
        print("Usage: uv run autolysis.py <dataset.csv>")
        sys.exit(1)

    file_path = sys.argv[1]
    dataset_name = os.path.splitext(os.path.basename(file_path))[0]
    output_dir = os.path.join(os.getcwd(), dataset_name)
    os.makedirs(output_dir, exist_ok=True)

    # Load and analyze dataset
    df = load_dataset(file_path)
    generate_visualizations(df, output_dir)
    create_correlation_matrix(df, output_dir)

    # Get analysis and story from LLM
    story = narrate_analysis(df, visualizations=["pairplot.png", "correlation_matrix.png"])
    summary = df.describe(include='all').to_string()

    # Save README
    save_readme(output_dir, dataset_name, summary, story, visualizations=["pairplot.png", "correlation_matrix.png"])

if __name__ == "__main__":
    main()