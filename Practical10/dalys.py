import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/Users/dongfeiyang/Desktop")
# print(os.getcwd) 
# Verify the current directory

dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv") #load the data
dalys_data.info() #get basic info about the DataFrame

print(dalys_data.describe())
# Max and min DALY will be shown in the "DALYs" column output
# First and last years will be shown in the "Year" column output

# print(dalys_data.iloc[0,3])
# print(dalys_data.iloc[2,0:5])
# print(dalys_data.iloc[0:2,:])
# print(dalys_data.iloc[0:10:2,0:5])
print (dalys_data.iloc[0:10,2]) 
# the third column (the year) for the first 10 rows
Afghanistan_data=dalys_data[dalys_data['Entity']=='Afghanistan']
print(Afghanistan_data.iloc[9,2])
#the 10th year for which DALYs were recorded in Afghanistan

# print(dalys_data.iloc[0:3,[0,1,3]])
# my_columns = [True, True, False, True]
# print(dalys_data.iloc[0:3,my_columns])
# print(dalys_data.loc[2:4,"Year"])

all_years = dalys_data.loc[:, "Year"] # All rows from Year column
print(all_years.head())
is1990 = dalys_data["Year"] == 1990 # every row where Year is 1990
print(is1990.head())  # Shows True/False for first few rows
dalys_1990 = dalys_data.loc[is1990, "DALYs"]
print(dalys_1990.head()) # All DALYs values from 1990
dalys_1990 = dalys_data.loc[dalys_data["Year"] == 1990, "DALYs"] #replace the "blabla" part
print(dalys_1990.head())

uk = dalys_data.loc[dalys_data["Entity"] == "United Kingdom", ["DALYs", "Year"]]
france = dalys_data.loc[dalys_data["Entity"] == "France", ["DALYs", "Year"]]
# Extract UK and France data
uk_mean = uk["DALYs"].mean()
france_mean = france["DALYs"].mean()
# Calculate mean DALYs
print(f"UK mean DALYs: {uk_mean:.2f}")
print(f"France mean DALYs: {france_mean:.2f}")
if uk_mean > france_mean:
    print("UK has higher mean DALYs than France")
else:
    print("France has higher mean DALYs than UK")
# Compare which is larger

plt.figure(figsize=(10, 5))
plt.plot(uk["Year"], uk["DALYs"], 'b+')  # Blue plus signs
plt.title("UK DALYs Over Time")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.show()
# Basic plot with different style options