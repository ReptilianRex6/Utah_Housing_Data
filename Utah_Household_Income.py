# importing 
import pandas as pd
import numpy as np
import datetime as dt
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pathlib import Path

## Read im median household income
median_income_path = Path("Resources/Median Household Income.csv")
median_income_df = pd.read_csv(median_income_path, parse_dates=True)

# Clean/organize data by:
# make column names useful
median_income_df.columns = ["Date", "Household Income"]
# ensure date time (didn't seem to work with parsing on read csv
median_income_df["Date"] = pd.to_datetime(median_income_df["Date"])
# simplify price column to thousands
median_income_df["Household Income"] = round(median_income_df["Household Income"]/1000, 2)
# slice data to start in 2000
median_income_df = median_income_df[-23:]

# make a monthly version using interpolation
# start with setting the new dataframe date range monthly
monthly_median_income_df = pd.DataFrame(pd.date_range(start='1/1/2000', end='1/1/2022', freq='MS'))
monthly_median_income_df.columns = ["Date"]

# merge the annual dataframe
monthly_median_income_df = monthly_median_income_df.merge(median_income_df, how='left')

# set the date to the index after successful merge
monthly_median_income_df = monthly_median_income_df.set_index("Date")

# interpolate data to fill in all NaN
monthly_median_income_df = monthly_median_income_df.interpolate().round(2)

## I like Matplot for a more polished look
med_income_fig, med_income_ax = plt.subplots(figsize=(12, 6))
med_income_ax.plot(monthly_median_income_df.index,
         monthly_median_income_df["Household Income"],
         color="darkorange",  label="Household Income")
med_income_ax.set_title("Median Household Income in Utah 2000-2022")
med_income_ax.set_xlabel("Data Granularity: Monthly (Annual Interpolated)")
med_income_ax.set_ylabel("Household Income in Thousands")
med_income_ax.xaxis.set_major_locator(mdates.YearLocator(2))
med_income_ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
med_income_ax.legend()
# and save the plot
plt.savefig(Path("Presentation Slide References/Median_Household_Income.png"))

# Export organized dataframe
monthly_median_income_df.to_csv(Path("Useful Dataframes/Median_Household_Income_Monthly_In_Thousands.csv"))
