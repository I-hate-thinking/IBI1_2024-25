# 1. Set the initial number of infected people
# 2. Set the daily growth rate
# 3. Total population: 91
# 4. Loop: Update the number of infected people every day
# 5. Display the number of people for the current day
# 6. Stop when the number of people is >= 91, output the number of days

infected = 5      
growth_rate = 0.4 
total = 91       
day = 1         

print(f"The{day}day: {infected} people infect")

while infected < total:
    day += 1
    infected = infected * (1 + growth_rate)
    if infected > total:
        infected = total
    print(f"The{day}day: {infected:.0f} people infect")

print(f"The entire infection process took a total of {day} day")
#The entire infection process took a total of 10 day