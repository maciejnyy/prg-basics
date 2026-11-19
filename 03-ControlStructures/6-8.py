person1_name = input('First person name: ')
person1_age = int(input('First person age: '))
person2_name = input('Second person name: ')
person2_age = int(input('Second person age: '))
if person1_age >= 18 and person2_age >= 18:
    print(f'Both {person1_name} and {person2_name} are adults')
else:
    print(f'Either {person1_name} or {person2_name} is not an adult')
