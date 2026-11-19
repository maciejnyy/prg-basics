###
# A program that prints your height both in cm and in feet and inches.
#
cm = 170
# convert to total inches (1 inch = 2.54 cm)
total_inches = round(cm / 2.54)
# calculate the number of feet (1 foot = 12 inches)
feet = total_inches // 12
# calculate the remaining inches
inches = total_inches % 12

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')
