# importing standard for this snippet
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pathlib import Path

## Note just starting with pre-cleaned data, could remove this is combined into one file
median_house_price_path = Path("Usefull Dataframes/Median_Home_Prices_Monthly_In_Thousands.csv")
median_house_price_df = pd.read_csv(median_house_price_path, parse_dates=True)
monthly_median_income_path = Path("Usefull Dataframes/Median_Household_Income_Monthly_In_Thousands.csv")
monthly_median_income_df = pd.read_csv(monthly_median_income_path, parse_dates=True)
# assure dates are correctly set as datestamps
median_house_price_df["Date"] = pd.to_datetime(median_house_price_df["Date"])
median_house_price_df = median_house_price_df.set_index("Date")
monthly_median_income_df["Date"] = pd.to_datetime(monthly_median_income_df["Date"])
monthly_median_income_df = monthly_median_income_df.set_index("Date")

# start of analysis for finding correlation between house price and income

# join dataframes on index (inner join just in case they are not 100% aligned)
price_vs_income_df = median_house_price_df.join(monthly_median_income_df, how="inner")

# plot line graphs togther (use twin axis to set double Y values)
price_vs_income_fig, price_vs_income_axa = plt.subplots(figsize=(12, 6))
price_vs_income_axa.set_title("Home Prices and Household Income Overlaid")
# X Axis
price_vs_income_axa.set_xlabel("Data Granularity: Monthly")
price_vs_income_axa.xaxis.set_major_locator(mdates.YearLocator(2))
price_vs_income_axa.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
# Left Y Axis
price_vs_income_axa.plot(price_vs_income_df.index,
         price_vs_income_df["Home Prices"],
         color="darkgreen",  label="Home Prices in Thousands (USD)")
price_vs_income_axa.set_ylabel("Home Price in Thouands $ (USD)", color="darkgreen")
price_vs_income_axa.tick_params(axis="y", labelcolor="darkgreen")
# Right Y Axis
price_vs_income_axb = price_vs_income_axa.twinx()
price_vs_income_axb.plot(price_vs_income_df.index,
         price_vs_income_df["Household Income"],
         color="darkorange",  label="Household Income (USD)")
price_vs_income_axb.set_ylabel("Household Income in Thouands $ (USD)", color="darkorange")
price_vs_income_axb.tick_params(axis="y", labelcolor="darkorange")
# combine legends into one
lines1, labels1 = price_vs_income_axa.get_legend_handles_labels()
lines2, labels2 = price_vs_income_axb.get_legend_handles_labels()
price_vs_income_axa.legend(lines1 + lines2, labels1 + labels2)
# and save plot
plt.savefig(Path("Output/Home_Prices_and_Household_Income_Overlaid.png"))

# And a scatter plot with regression line
price_vs_income_fig2, price_vs_income_ax2 = plt.subplots(figsize=(12, 6))
price_vs_income_ax2.scatter(price_vs_income_df["Household Income"],
                            price_vs_income_df["Home Prices"],
                            marker=".", color="lightsteelblue")
price_vs_income_ax2.set_title("Correlation of Home Prices to Household Income")
price_vs_income_ax2.set_xlabel("Household Income in Thousands $ (USD)")
price_vs_income_ax2.set_ylabel("Home Prices in Thousands $ (USD)")
# fit regression and plot line
slope, yinter = np.polyfit(price_vs_income_df["Household Income"],
                           price_vs_income_df["Home Prices"], 1)
price_vs_income_ax2.plot(price_vs_income_df["Household Income"],
                         slope*price_vs_income_df["Household Income"] + yinter,
                         color="darkgreen")
# explain it
price_vs_income_corr = price_vs_income_df["Home Prices"].corr(price_vs_income_df["Household Income"])
pvi_corr_text = f"""Correlation Coefficient: {price_vs_income_corr}

Slope: {slope}
Y-Intercept: {yinter}
"""
price_vs_income_fig2.text(0.5, 0.70, pvi_corr_text, ha="center", color="darkgreen")
plt.savefig(Path("Output/Correlation_of_Home_Prices_to_Household_Income.png"))
