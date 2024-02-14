# importing basics
import pandas as pd
import numpy as np
import datetime as dt
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pathlib import Path

## Let's prep up population to monthly
population_path = Path("Resources/utah population 2000-2022 neilsberg.csv")
population_df = pd.read_csv(population_path, parse_dates=True)

# Clean/organize data by:
# drop columns not needed for this analysis
population_df = population_df.drop(columns=["Year on Year Change", "Change in Percent"])
# make column names useful
population_df.columns = ["Date", "Population"]
# ensure date time (didn't seem to work with parsing on read csv)
population_df["Date"] = pd.to_datetime(population_df["Date"], format="%Y")
# remove commas in population count before convert
population_df["Population"] = population_df["Population"].apply(lambda x: x.replace(",", ""))
# ensure population is integer
population_df["Population"] = population_df["Population"].astype(dtype="int")

# make a monthly version using interpolation
# start with setting the new dataframe date range monthly
monthly_population_df = pd.DataFrame(pd.date_range(start='1/1/2000', end='1/1/2022', freq='MS'))
monthly_population_df.columns = ["Date"]

# merge the annual dataframe
monthly_population_df = monthly_population_df.merge(population_df, how='left')

# interpolate population data to fill in all NaN
monthly_population_df = monthly_population_df.interpolate().round(0)

# set date as index
monthly_population_df = monthly_population_df.set_index("Date")

# claculate monthly population growth --
#   note interpolation this way keeps growth even each month of the year, not totally accurate but good enough
monthly_population_df["Population Growth"] = monthly_population_df["Population"].diff()

# fill the first column (NaN) as 0, no precent change first month (got to start somewhere)
monthly_population_df["Population Growth"] = monthly_population_df["Population Growth"].fillna(0)

# Now pull in monthly permits
monthly_permits_path = Path("Resources/permits.csv")
monthly_permits_df = pd.read_csv(monthly_permits_path, parse_dates=True)

# Clean/organize data by:
# make column names useful
monthly_permits_df.columns = ["Date", "Building Permits"]
# ensure date time (didn't seem to work with parsing on read csv)
monthly_permits_df["Date"] = pd.to_datetime(monthly_permits_df["Date"])
# set date as index
monthly_permits_df = monthly_permits_df.set_index("Date")

# join dataframes on the index (inner cuts out any addiional missing data)
monthly_pop_vs_permits_df = monthly_population_df.join(monthly_permits_df, how='inner')

# Putting an average 3 people in each building unit to find number of units needed
monthly_pop_vs_permits_df["Build Requirements (3/unit)"] = monthly_pop_vs_permits_df["Population Growth"] / 3

# Track the monthly totals via cumulative sum for each column
build_vs_requried_cum_sum_df =  pd.DataFrame(monthly_pop_vs_permits_df["Building Permits"].cumsum())
build_vs_requried_cum_sum_df["Total Required"] = monthly_pop_vs_permits_df["Build Requirements (3/unit)"].cumsum()
build_vs_requried_cum_sum_df.columns = ["Total Permits", "Total Required"]

# calculate surplus (more houses built than needed) vs. shortfall (fewer houses built than needed)
build_vs_requried_cum_sum_df["Surplus or Shortfall"] = build_vs_requried_cum_sum_df["Total Permits"] - build_vs_requried_cum_sum_df["Total Required"]

# isolate just the surplus or shortfall calumn to plot graph
surpluse_or_shortfall_df = build_vs_requried_cum_sum_df.filter(["Surplus or Shortfall"], axis=1)

## I like Matplot for a more polished look
sos_fig, sos_ax = plt.subplots(figsize=(12, 6))
sos_ax.plot(surpluse_or_shortfall_df.index,
            surpluse_or_shortfall_df["Surplus or Shortfall"],
            color="r",  label="Surplus (>0) or Shortfall (<0)")
sos_ax.set_title("Actual Building - Required Building\n(to Keep Up with Population Growth)")
sos_ax.set_xlabel("Data Granularity: Monthly (Some Annual Interpolated)")
sos_ax.set_ylabel("Surplus (+) or Shortfall (-) of Needed Housing")
sos_fig_note = "This data presumes housing 3 persons per unit, which is the current Sate average."
sos_fig.text(0.5, 0.13, sos_fig_note, ha='center')
sos_ax.xaxis.set_major_locator(mdates.YearLocator(2))
sos_ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
sos_ax.legend()
plt.axhline(y=0, color="k", linestyle="-")
plt.autoscale(tight=True)
# and save the plot
plt.savefig(Path("Presentation Slide References/Housing_Shortfall.png"))
