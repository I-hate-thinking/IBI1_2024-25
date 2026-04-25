import matplotlib.pyplot as plt

#population data (in millions)
data = {
    "UK": (66.7, 69.2),
    "China": (1426, 1410),
    "Italy": (59.4, 58.9),
    "Brazil": (208.6, 212.0),
    "USA": (331.6, 340.1)
}

#calculate the rate of change
changes = {}
for country, (pop2020, pop2024) in data.items():
    change = ((pop2024 - pop2020) / pop2020) * 100
    changes[country] = change

#output each country
print("Population percentage change (2020-2024):")
for c, val in changes.items():
    print(f"{c}: {val:.2f}%")

#sort
sorted_changes = sorted(changes.items(), key=lambda x: x[1], reverse=True)
print("\nSorted (largest increase to largest decrease):")
for c, val in sorted_changes:
    print(f"{c}: {val:.2f}%")

#largest increase/largest decrease
max_inc = sorted_changes[0][0]
max_dec = sorted_changes[-1][0]
print(f"\nLargest increase: {max_inc}")
print(f"Largest decrease: {max_dec}")

#draw the bar chart
countries = [x[0] for x in sorted_changes]
values = [x[1] for x in sorted_changes]

plt.bar(countries, values, color='orange')
plt.title("Population Percentage Change (2020-2024)")
plt.xlabel("Country")
plt.ylabel("Percentage Change (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()