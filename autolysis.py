# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pandas",
#   "matplotlib",
#   "seaborn",
#   "openai",
# ]
# ///

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import openai
import sys

my_api= "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIyZjMwMDMxNTdAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.jqgA4t_kF3xuPBBPlGeLSKobS64VlLoTFSdh9MUMchQ"
# Set up OpenAI API key
AIPROXY_TOKEN = os.environ.get(my_api)
openai.api_key = AIPROXY_TOKEN

def load_and_explore(file_path):
    """Load the dataset and provide a basic summary."""
    data = pd.read_csv(file_path, encoding='ISO-8859-1')
    summary = {
        "shape": data.shape,
        "columns": data.dtypes.to_dict(),
        "missing_values": data.isnull().sum().to_dict(),
        "summary_stats": data.describe(include="all").to_dict(),
    }
    return data, summary

def analyze_data(data):
    """Perform general analysis on the dataset."""
    analysis = {}

    # Missing value analysis
    analysis["missing_values"] = data.isnull().sum().to_dict()

    # Correlation matrix
    numeric_data = data.select_dtypes(include="number")
    if not numeric_data.empty:
        analysis["correlation_matrix"] = numeric_data.corr().to_dict()

    # Basic statistical overview
    analysis["summary_statistics"] = numeric_data.describe().to_dict()

    return analysis

def generate_visualizations(data, output_prefix):
    """Generate and save visualizations."""
    numeric_data = data.select_dtypes(include="number")
    
    # Correlation heatmap
    if not numeric_data.empty:
        plt.figure(figsize=(10, 8))
        sns.heatmap(numeric_data.corr(), annot=True, fmt=".2f", cmap="coolwarm")
        plt.title("Correlation Matrix Heatmap")
        plt.savefig(f"{output_prefix}_correlation.png")
        plt.close()

    # Missing values bar chart
    missing = data.isnull().sum()
    if missing.sum() > 0:
        plt.figure(figsize=(10, 6))
        missing[missing > 0].plot(kind="bar", color="skyblue")
        plt.title("Missing Values by Column")
        plt.ylabel("Count")
        plt.savefig(f"{output_prefix}_missing.png")
        plt.close()

def query_llm(prompt):
    """Query the LLM with a specific prompt."""
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000,
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error querying LLM: {e}"

def narrate_story(summary, analysis, dataset_name, visualizations):
    """Generate a story from the analysis using the LLM."""
    prompt = f"""
    The dataset analyzed is named {dataset_name}.
    Here is a summary of the dataset:
    {summary}
    
    Here are the key findings from the analysis:
    {analysis}
    
    Visualizations have been created to support the analysis:
    {visualizations}

    Write a clear and engaging story about the analysis, highlighting key insights and their implications.
    """
    return query_llm(prompt)

def save_readme(dataset_name, story, visualizations):
    """Save the narrative and visualization links to README.md."""
    with open("README.md", "w") as f:
        f.write(f"# Analysis of {dataset_name}\n\n")
        f.write(story)
        f.write("\n\n## Visualizations\n")
        for viz in visualizations:
            f.write(f"![{viz}]({viz})\n")

def main():
    if len(sys.argv) != 2:
        print("Usage: uv run autolysis.py <dataset.csv>")
        sys.exit(1)

    file_path = sys.argv[1]
    dataset_name = file_path.split(".")[0]

    # Load and explore
    data, summary = load_and_explore(file_path)

    # Analyze
    analysis = analyze_data(data)

    # Generate visualizations
    output_prefix = dataset_name
    generate_visualizations(data, output_prefix)
    visualizations = [f"{output_prefix}_correlation.png", f"{output_prefix}_missing.png"]

    # Narrate the story
    story = narrate_story(summary, analysis, dataset_name, visualizations)

    # Save README.md
    save_readme(dataset_name, story, visualizations)
    print("Analysis complete. Check README.md and visualizations.")

if __name__ == "__main__":
    main()