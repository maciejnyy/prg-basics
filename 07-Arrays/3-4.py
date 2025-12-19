numbers = [-15, 8, -31, 47, -2, 19]

# Assume the first element is both min and max
minimum = numbers[0]
maximum = numbers[0]

# Traverse the list
for num in numbers:
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

print("Minimum number:", minimum)
print("Maximum number:", maximum)