import matplotlib.pyplot as plt

heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]

# 1. the number of patients and the mean heart rate
num_patients = len(heart_rates)
mean_hr = sum(heart_rates) / num_patients
print(f"Total patients: {num_patients}, Mean heart rate: {mean_hr:.2f} bpm")

# 2. classification and counting
low = 0
normal = 0
high = 0

for hr in heart_rates:
    if hr < 60:
        low += 1
    elif hr > 120:
        high += 1
    else:
        normal += 1

print(f"\nLow: {low}, Normal: {normal}, High: {high}")

# find the largest group
categories = {"Low": low, "Normal": normal, "High": high}
largest = max(categories, key=categories.get)
print(f"The largest category is: {largest}")

# 3. produce a pie chart
labels = ["Low", "Normal", "High"]
sizes = [low, normal, high]
colors = ["lightblue", "lightgreen", "salmon"]

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%')
plt.title("Heart Rate Category Distribution")
plt.show()