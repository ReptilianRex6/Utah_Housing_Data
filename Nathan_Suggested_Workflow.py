## Note on comment style, double ## is for our teamwork only, should be removed in final

# Start with some tools of Data Analysis
import pandas as pd
import numpy as np
import datetime as dt
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Read in source data for home prices

# Organize/clean data structure
## specifically:
## 1. if we get quarterly we will need to use interpolation to estimate monthly
## 2. determine if we want to cut out at 2022 for later prophet

# Save plot showing increase in prices

# Save plot showing trend line

# Read in sourse data from income

# Organize/clean data structure
## same as needed above

# Save plot showing Incmoe

## Maybe calculating percent change and another plot?

# Read in source data for population

# Organize/clean data structure
## same necessities as above

# Save plot showing increase population

# Calculate percent change and another plot (as we discussed relevancy)

# Read in source data for interest rates

# Organize/clean data structure
## sames needs as above

# Save plot showing mortgage interest rates over time (30 year fixed)

# combine dataframes

# Scatter plot with regression line x income, y house price

# Scatter plot with regression line x population, y house price

# Scatter plot with regression line x interst, y house price

# And for the numbers let's calculate and display correlation coefficents

## Now if we want to do prophet, here is the best place

