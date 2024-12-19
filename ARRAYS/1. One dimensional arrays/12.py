###
# Program to calculate the most expensive expense category
#
categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

# Find the index of the highest expense
max_expense_index = expenses.index(max(expenses))

# Get the category corresponding to the highest expense
most_expensive_category = categories[max_expense_index]

# Print the most expensive category and its expense
print("The most expensive category is:", most_expensive_category)
print("Expense amount:", expenses[max_expense_index])
