# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
   ["Pancakes", "Sandwich", "Steak"],
   ["Smoothie", "Chicken Wrap", "Salmon"],
   ["Eggs", "Pasta", "Soup"],
   ["Toast", "Burrito", "Pizza"],
   ["Cereal", "Salad", "Fish Tacos"],
   ["Bagel", "Rice and Beans", "Stir-fry"]
]

# Funkcja zwracająca nazwę dnia tygodnia
def weekday(n):
   weekdays = ["Monday", "Tuesday", "Wednesday",
      "Thursday", "Friday", "Saturday", "Sunday"]
   return weekdays[n-1]

# Funkcja zwracająca posiłki na dany dzień
def day_meal_plan(meal_plan, day_number):
   meals = meal_plan[day_number - 1]
   return ", ".join(meals)

# Wydrukowanie planu posiłków na cały tydzień
print("WEEKLY MEAL PLAN")
print("(Breakfast, Lunch, Dinner)")
print("==========================")

for i in range(1, 8):
   print(f"{weekday(i)}: {day_meal_plan(meal_plan, i)}")
