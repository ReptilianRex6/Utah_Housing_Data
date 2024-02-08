# importing 
import pandas as pd
import numpy as np
import datetime as dt
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pathlib import Path

## Note Ryan's data will need to be merged to main and put in Resources for this code to work
median_house_price_path = Path("Resources/UTUCSFRCONDOSMSAMID.csv")
median_house_price_df = pd.read_csv(median_house_price_path, parse_dates=True)

# Clean/organize data by:
# make column names useful
median_house_price_df.columns = ["Date", "Home Prices"]
# simplify price column to thousands
median_house_price_df["Home Prices"] = round(median_house_price_df["Home Prices"]/1000, 2)
# set date as index
median_house_price_df = median_house_price_df.set_index("Date")

# verify dataframe with dates
median_house_price_df.head()

## I like Matplot for a more polished look
med_house_fig, med_house_ax = plt.subplots(figsize=(12, 6))
med_house_ax.plot(median_house_price_df.index,
         median_house_price_df["Home Prices"],
         color="darkgreen",  label="Home Prices in Thousands")
med_house_ax.set_title("Median Home Prices in Utah 2000-2023")
med_house_ax.set_xlabel("Monthly")
med_house_ax.set_ylabel("Home Prices in Thousands")
med_house_ax.xaxis.set_major_locator(mdates.YearLocator(1,month=1,day=1))
med_house_ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
med_house_ax.legend()
plt.autoscale(tight=True)
plt.savefig(Path("Output/Median_Home_Price_Increase.png"))