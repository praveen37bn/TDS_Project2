# Analysis of media

## Summary
```
             date language   type              title                 by      overall      quality  repeatability
count        2553     2652   2652               2652               2390  2652.000000  2652.000000    2652.000000
unique       2055       11      8               2312               1528          NaN          NaN            NaN
top     21-May-06  English  movie  Kanda Naal Mudhal  Kiefer Sutherland          NaN          NaN            NaN
freq            8     1306   2211                  9                 48          NaN          NaN            NaN
mean          NaN      NaN    NaN                NaN                NaN     3.047511     3.209276       1.494721
std           NaN      NaN    NaN                NaN                NaN     0.762180     0.796743       0.598289
min           NaN      NaN    NaN                NaN                NaN     1.000000     1.000000       1.000000
25%           NaN      NaN    NaN                NaN                NaN     3.000000     3.000000       1.000000
50%           NaN      NaN    NaN                NaN                NaN     3.000000     3.000000       1.000000
75%           NaN      NaN    NaN                NaN                NaN     3.000000     4.000000       2.000000
max           NaN      NaN    NaN                NaN                NaN     5.000000     5.000000       3.000000
```

## Narrative
Based on your dataset, comprising 2652 rows and 8 columns, we can summarize key insights and suggest potential actions as follows:

### Key Insights:

1. **Data Completeness**:
   - Out of 2652 rows, there are 2553 entries for the 'date', 2390 for the 'by' field, indicating some missing data, especially in the 'by' column. Efforts should be made to either fill these gaps or handle them in analysis.
   - The unique values in 'language' (11) and 'type' (8) suggest a diverse dataset possibly representative of different cultures or media formats.

2. **Language Distribution**:
   - The most frequent language is English, occurring 1306 times. This highlights a potential bias toward English content, which might indicate that the dataset is skewed toward certain cultural outputs.

3. **Title Variability**:
   - There are 2312 unique titles despite 2652 entries, implying that many titles do not have multiple entries, which could be due to some being judged, reviewed, or captured only once.

4. **Quality and Ratings**:
   - The 'overall' score has a mean of approximately 3.05, with a standard deviation of 0.76. The maximum score is 5, indicating that there are reviews reaching very high ratings. 
   - The 'quality' score's mean is slightly higher at 3.21, suggesting that overall perceptions of quality slightly exceed general ratings.

5. **Repeatability**:
   - The 'repeatability' score has a lower mean of approximately 1.49, suggesting that the content may lack aspects that encourage repeated viewing or engagement.

6. **Rating Distributions**:
   - The quartiles of the 'overall' and 'quality' scores suggest that most ratings are around the middle of the scale (mostly between 3 and 4), which can indicate a tendency towards mediocre reviews.

### Suggestions for Action:

1. **Data Integrity Measures**:
   - Consider strategies for dealing with missing data in the 'by' column, such as imputation or aggregating by language/type if analysis allows.
  
2. **Content Diversity**:
   - Since English is the most prevalent language, consider developing or promoting content from underrepresented languages to enhance diversity and reach a broader audience.

3. **Enhancing Content**:
   - Given the lower repeatability score, investigate the reasons behind it.

![/Users/praveenkumar/Desktop/TDS/TDS_Project2/media/pairplot.png](/Users/praveenkumar/Desktop/TDS/TDS_Project2/media/pairplot.png)
