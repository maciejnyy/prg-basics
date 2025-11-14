###
# Sums numbers entered by user
#
total_sum = 0
number_counter = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    number_counter += 1
    mean = total_sum / number_counter

print(f"The total sum of the numbers is: {total_sum}")
print(f"The arithmetic mean of the numbers is: {mean}")
