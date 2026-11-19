import converters

print('### Test converters')
print(f'Three meters is {converters.m_to_cm(3)}cm')
print(f'20 centimeters is {converters.cm_to_inches(20):.2f} inches')
print(f'5 feet and 8 inches is {converters.feet_and_inches_to_cm(5, 8):.2f} cm')
