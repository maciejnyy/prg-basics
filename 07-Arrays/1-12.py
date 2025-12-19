categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

# find the index of the highest expense
max_index = expenses.index(max(expenses))

# get the corresponding category
most_expensive_category = categories[max_index]

print("Most expensive category:", most_expensive_category)