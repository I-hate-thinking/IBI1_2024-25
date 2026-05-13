import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Set the working directory
os.chdir("/Users/dongfeiyang/Desktop/IBI1_2025/IBI1_2025-26/IBI1_2024-25/Practical10")
# Confirm the existence of the csv file
print("Files in directory:", os.listdir())

# 2. reads the data
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
# Check the previous few lines
print("\n=== Head of data ===")
print(dalys_data.head())

# data information
print("\n=== Data info ===")
print(dalys_data.info())
# digest of statistics
print("\n=== Summary stats ===")
print(dalys_data.describe())

# 3. First 10 rows: find the year with the maximum value in the first 10 years of Afghanistan
# Third and fourth columns: Year(2), DALYs(3)
subset_10 = dalys_data.iloc[0:10, [2, 3]]
print("\n=== First 10 rows: Year + DALYs ===")
print(subset_10)
# The year with the highest number of Disability-Adjusted Life Years (DALYs) in Afghanistan over the past 10 years
afghan_10 = dalys_data.iloc[0:10, :]
max_idx = afghan_10["DALYs"].idxmax()
max_year = afghan_10.loc[max_idx, "Year"]
print(f"\n# Afghanistan max DALYs in first 10 years: {max_year}")
# max DALYs in first 10 years: 1998

# 4. Select all data from Zimbabwe, specifying the start and end years
zimbabwe = dalys_data.loc[dalys_data["Entity"] == "Zimbabwe", :]
print("\n=== Zimbabwe data ===")
print(zimbabwe.head())
print(f"# Zimbabwe data range: {zimbabwe['Year'].min()} - {zimbabwe['Year'].max()}")
# Zimbabwe data range: 1990 - 2019

# 5. 2019: Countries with the highest and lowest DALYs
data_2019 = dalys_data.loc[dalys_data["Year"] == 2019, ["Entity", "DALYs"]]
max_2019 = data_2019.loc[data_2019["DALYs"].idxmax()]
min_2019 = data_2019.loc[data_2019["DALYs"].idxmin()]
print("\n=== 2019 max/min DALYs ===")
print(f"# Max: {max_2019['Entity']} ({max_2019['DALYs']})")
print(f"# Min: {min_2019['Entity']} ({min_2019['DALYs']})")
# Max: Lesotho (90771.64)
# Min: Singapore (15045.11)

# 6. Draw a time series of a country (using the country with the highest value)
country_max = max_2019["Entity"]
country_data = dalys_data.loc[dalys_data["Entity"] == country_max, :]

plt.figure(figsize=(10, 5))
plt.plot(country_data["Year"], country_data["DALYs"], marker='o', linestyle='-', color='blue')
plt.title(f"DALYs over time: {country_max}")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("daly_trend_max_country.png", dpi=300)
plt.show()

# 7. Self-selected question: Box plot of global DALYs distribution in 2019
plt.figure(figsize=(8, 5))
plt.boxplot(data_2019["DALYs"])
plt.title("Global DALYs distribution (2019)")
plt.ylabel("DALYs")
plt.tight_layout()
plt.savefig("daly_boxplot_2019.png", dpi=300)
plt.show()