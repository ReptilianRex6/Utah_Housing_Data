# Utah Housing Data Analysis

   ### CONTENTS
**[Analysis Team](#analysis-team)**<br>
**[Hypothesis and Questions](#hypothesis-and-questions)**<br>
**[Data Sources](#data-sources)**<br>
**[Methodology](#methodology)**<br>
**[Repository Assets](#repository-assets)**<br>
**[Findings/Conclusion](#findingsconclusion)**<br>
**[Prophet](#prophet)**<br>

## Analysis Team

This analysis of Utah housing data is the collective work of the following team members as part of University of Utah's AI Bootcamp by edX:
- Zac Baxter, *talent acquisition*
- Ethan Bennett, *machinist and computer enthusiast*
- Ryan Mosher, *mortgage and bond specialist*
- Stephen Singletary, *a tech enthusiast reskilling to break into data analysis*
- Nathan Tyler, *a well-rounded computer specialist*

## Hypothesis and Questions

### Hypothesis

We believe that the average price of a home in Utah has risen significantly over time due to a combination of rising incomes, population growth, and changes in interest rates.

### Questions

To test our hypothesis the analysis will answer:
1. What is the average price of a home in Utah over time?
2. What is the average income in Utah over time?
3. What is the population of Utah over time?
4. How have mortgage interest rates in Utah changed over time?
5. What is the relationship between the average price of a home, average income, interest rates, and population?

## Data Sources

The data used in this analysis will be obtained from:
- [Federal Reserve Economic Data (FRED)](https://fred.stlouisfed.org/)
- [Neilsberg Research](https://www.neilsberg.com/)

## Methodology

Utilizing modern data analysis tools offered in the Python* programming language, several Python scripts (.py) and Jupyter Notebooks (.ipynb)  contain the code to that reads, cleans, organizes, and plots the data. These .py files can be run from a terminal or IDE such as VS Code. The notebooks could  be run in Jupyter Lab or VS Code with extensions.

*The Python environment should be setup to include:
- Python 3.10
- Pandas
- Matplotlib
- Scipy
- Prophet

The analysis will be summarized below in the **[Findings](#findings)** section and a final presentation will be put together using using Google Slides (in a PowerPoint format).

## Repository Assets

### Source Code

- Correlations.ipnb
- Housing_Shortfall.py
- Income_Correlation.py
- Permits to pop compare.ipynb
- Prophecies_workshop.ipynb
- Prophecy_final_work.py
- Stephen_Group_Project_Notebook.ipynb
- Utah_Household_Income.py
- Utah_Household_Prices.py

### Resources

- 10-year-treasury-bond-rate-yield-chart.csv
- Building permits for single family.csv
- Median Home Pricing.csv
- Median Household Income.csv
- Mortgage Rates 30y Fixed.csv
- Real Median Household Income.csv
- Resident Population in Utah.csc
- Utah State House Price Index.csv
- filled_df.csv
- Utah population 2000-2022 neilsberg.csv

### Other Folders

Additional folders in this repository are storing random working code snippets, cleaned data, and test files which can be ignored.

## Findings/Conclusion

We found that generally income is strongly correlated with home prices, as income increases home prices increases will lag behind.

![Income to Home Price Comparison/Correlation](https://github.com/ReptilianRex6/Utah_Housing_Data/blob/main/Presentation%20Slide%20References/Home_Prices_and_Household_Income_Overlaid.png)

We found a negative correlation between interest rates and home prices. As interest rates fall, home prices rise.

![Interest Rates to Home Price Comparison/Correlation](https://github.com/ReptilianRex6/Utah_Housing_Data/blob/main/Presentation%20Slide%20References/best_home_prices_vs_interest_rates_720.png)

When reviewing building permits vs. population growth we saw the likelihood of a disparity between new construction and population growth.

![Building Permits vs. Population Growth](https://github.com/ReptilianRex6/Utah_Housing_Data/blob/main/Presentation%20Slide%20References/PopulationvsPermits.png)

This led us to want to calculate just how much of a disparity there was. Given that the average housing unit in Utah houses three persons, we performed a cumulative summation of building permits and population growth. We found that there is a 41,000 shortfall of new housing units built since the year 2000.

![Housing Surplus or Shortfall](https://github.com/ReptilianRex6/Utah_Housing_Data/blob/main/Presentation%20Slide%20References/Housing_Shortfall.png)

In the end we also wanted to look at the raw correlations between all the data points in question.

![Correlation_Table](https://github.com/ReptilianRex6/Utah_Housing_Data/blob/main/Presentation%20Slide%20References/Correlation_Table.png)

From these data points we can answer:
1. The average price of a home in Utah has increased over time. More significantly in the past few years.

2. The average income of Utah households has also increased over time.

3. Utah is a steadily growing state.

4. Mortgage interest rates fluctuate consistently, but moved down for a long time helping drive up the costs of homes.

5. There are strong positive correlations between home prices and income, and building permits issued. There is a medium negative correlation between interest rates and home prices, but a strong correlation between interest rates and building permits.

## Prophet

We also used the Prophet Python package with the data ending in 2022 to predict the future in 2023 and compared it to the real data to see how well Prophet predicts the future.