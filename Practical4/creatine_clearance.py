# 1. Input age, weight, gender and Cr value
# 2. Check if the input is valid
# 3. If valid, calculate; otherwise, display error message

age = 25
weight = 60
gender = "female"
cr = 80

#check the input
valid = True
if age >= 100:
    print("Error: Age must be less than 100.")
    valid = False
if weight <=20 or weight >=80:
    print("Error: The weight must be between 20 and 80.")
    valid = False
if cr <=0 or cr >=100:
    print("Error: Cr must be within the range of 0 to 100.")
    valid = False
if gender not in ["male","female"]:
    print('Error: Gender must be either "male" or "female".')
    valid = False

# calculate
if valid:
    if gender == "male":
        crcl = (140 - age) * weight / (72 * cr)
    else:
        crcl = (140 - age) * weight / (72 * cr) * 0.85
    print("Creatine_Clearance CrCl =", crcl)