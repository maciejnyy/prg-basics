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

# Returns a week day name
def weekday(n):
   weekdays = ["Monday", "Tuesday", "Wednesday",
      "Thursday", "Friday", "Saturday", "Sunday"]
   return weekdays[n]

# Returns a string with day meal names
# separated by comma
def day_meal_plan(meal_plan, day_number):
   
   week_plan = []
   for week in meal_plan: 
      plan = ""
      for day in week:
        plan += day + ", "
      week_plan.append(plan)
      
   return week_plan[day_number]

# Prints weekly meal plan
for i in range(7): 
    print(weekday(i),":", day_meal_plan(meal_plan, i))
...
...