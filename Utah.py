# Analysis and Conclusion:
# Hypothesis: The average price of a home in Utah is higher over time due to a combination of rising incomes and population growth.
# Questions: 
# 1. What is the average price of a home in Utah over time?
# 2. What is the average income in Utah over time?
# 3. What is the population of Utah over time?
# 4. What is the relationship between the average price of a home, average income, and population?

# Importing the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Reading in the data from FRED and storing it in a dataframe
Real_Median_Household_Income = pd.read_csv('Real Median Household Income')
Average_Price_of_a_Home = pd.read_csv('Utah State House Price Index')
Population = pd.read_csv('Resident Population In Utah')

# Visualizing the Data:

# Fig. 1 - Average Price of a Home in Utah Over Time

Fig1 = Average_Price_of_a_Home["DATE", "MEHOINUSUTA672N"].plot(x="DATE", y="MEHOINUSUTA672N", title="Real Median Household Income in Utah Over Time", xlabel="Year", ylabel="Real Median Household Income in Utah")
print(Fig1)
# Fig. 2 - Average Income in Utah Over Time

Fig2 = Real_Median_Household_Income["DATE", "UTSTHPI"].plot(x="DATE", y="UTSTHPI", title="Average Income in Utah Over Time", xlabel="Year", ylabel="Average Income in Utah")
print(Fig2)
# Fig. 3 - Population of Utah Over Time

Fig3 = Population["DATE", "UTPOP"].plot(x="DATE", y="UTPOP", title="Population in Utah Over Time", xlabel="Year", ylabel="Population")
print(Fig3)
# Fig. 4 - Relationship Between the Average Price of a Home, Average Income, and Population 

Fig4 = Real_Median_Household_Income["DATE", "MEHOINUSUTA672N"].plot(x="DATE", y="MEHOINUSUTA672N", title="Real Median Household Income in Utah Over Time", xlabel="Year", ylabel="Real Median Household Income in Utah")

