class food_item:
    """Food items: Name, Calories, Protein, Carbohydrates, Fat"""
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

def daily_nutrition(food_list):
    """
    Receive the list of recipients of food, and calculate the total intake over 24 hours
    Output a warning when the calorie count is over 2500 or the fat content is more than 90g
    """
    total_cal = 0
    total_pro = 0
    total_car = 0
    total_fat = 0

    for food in food_list:
        total_cal += food.calories
        total_pro += food.protein
        total_car += food.carbs
        total_fat += food.fat

    print("=== Daily Nutrition Summary ===")
    print(f"Total Calories: {total_cal}")
    print(f"Total Protein: {total_pro} g")
    print(f"Total Carbs: {total_car} g")
    print(f"Total Fat: {total_fat} g")

    if total_cal > 2500:
        print("⚠️ Warning: Excessive calorie intake (>2500)")
    if total_fat > 90:
        print("⚠️ Warning: Excessive fat intake (>90g)")

# example
if __name__ == "__main__":
    # Create a food object
    apple = food_item("Apple", 60, 0.3, 15, 0.5)
    egg = food_item("Egg", 70, 6, 0.5, 5)
    burger = food_item("Burger", 500, 25, 30, 25)
    # List of foods consumed in one day
    daily_food = [apple, egg, burger]
    # Calculation summary
    daily_nutrition(daily_food)