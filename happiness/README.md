# Analysis of happiness

## Summary
```
       Country name         year  Life Ladder  Log GDP per capita  Social support  Healthy life expectancy at birth  Freedom to make life choices   Generosity  Perceptions of corruption  Positive affect  Negative affect
count          2363  2363.000000  2363.000000         2335.000000     2350.000000                       2300.000000                   2327.000000  2282.000000                2238.000000      2339.000000      2347.000000
unique          165          NaN          NaN                 NaN             NaN                               NaN                           NaN          NaN                        NaN              NaN              NaN
top         Lebanon          NaN          NaN                 NaN             NaN                               NaN                           NaN          NaN                        NaN              NaN              NaN
freq             18          NaN          NaN                 NaN             NaN                               NaN                           NaN          NaN                        NaN              NaN              NaN
mean            NaN  2014.763860     5.483566            9.399671        0.809369                         63.401828                      0.750282     0.000098                   0.743971         0.651882         0.273151
std             NaN     5.059436     1.125522            1.152069        0.121212                          6.842644                      0.139357     0.161388                   0.184865         0.106240         0.087131
min             NaN  2005.000000     1.281000            5.527000        0.228000                          6.720000                      0.228000    -0.340000                   0.035000         0.179000         0.083000
25%             NaN  2011.000000     4.647000            8.506500        0.744000                         59.195000                      0.661000    -0.112000                   0.687000         0.572000         0.209000
50%             NaN  2015.000000     5.449000            9.503000        0.834500                         65.100000                      0.771000    -0.022000                   0.798500         0.663000         0.262000
75%             NaN  2019.000000     6.323500           10.392500        0.904000                         68.552500                      0.862000     0.093750                   0.867750         0.737000         0.326000
max             NaN  2023.000000     8.019000           11.676000        0.987000                         74.600000                      0.985000     0.700000                   0.983000         0.884000         0.705000
```

## Narrative
Based on the provided dataset, here are key insights and suggested actions derived from the data analysis:

### Key Insights:

1. **General Trends**:
   - The dataset contains 2363 entries over a range of years from 2005 to 2023.
   - The mean life ladder score, which indicates subjective well-being, is approximately 5.48, with scores ranging from a minimum of 1.28 to a maximum of 8.02 across different countries.

2. **Life Ladder**:
   - The life ladder values show substantial variability, indicating significant differences in happiness or well-being perceptions among countries.
   - Only about 5.6% of entries have a Life Ladder score below the 25th percentile (4.65).

3. **Economic Factors** (Log GDP per Capita):
   - The average log GDP per capita is around 9.40, with a minimum GDP per capita of around 5.53 and a maximum of about 11.68, suggesting a diverse economic landscape.
   - It is important to correlate this with Life Ladder scores to help quantify the impact of economic well-being on perceived happiness.

4. **Social Support**:
   - The average social support score stands at 0.81, with minimum and maximum values of 0.23 and 0.99 respectively. This indicates that social relationships might play a significant role in overall well-being.
   - The correlation between social support and Life Ladder scores could be explored to understand if support systems effectively contribute to life satisfaction.

5. **Health and Life Expectancy**:
   - The average healthy life expectancy at birth is approximately 63.4 years, with considerable variation. This suggests that health outcomes have implications for well-being as reflected in Life Ladder scores.
   - A potential avenue for further investigation could address the impact of healthier lifestyles and access to healthcare on overall life satisfaction.

6. **Freedom to Choose**:
   - The mean score for 'Freedom to make life choices' is around 0.75, with the upper quartile being significantly higher. Societal and governmental structures in countries with lower scores could be assessed for limitations on personal freedoms.

7. **Corruption and Generosity**:
   - The perceptions of corruption reveal a mean score of 0.74, while the average generosity score is near zero (0.0001), indicating widespread poverty or lack of philanthropic engagement in the dataset.
   - Countries with lower corruption perceptions

![/Users/praveenkumar/Desktop/TDS/TDS_Project2/happiness/pairplot.png](/Users/praveenkumar/Desktop/TDS/TDS_Project2/happiness/pairplot.png)
