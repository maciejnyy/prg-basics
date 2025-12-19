def amount_to_pay(value):
    i = 0
    money_counter = 0
    while value > 0:
        if value >= 5:
            value -= 5
            money_counter += 1
        elif value >= 2 and value < 5:
            value -= 2
            money_counter += 1
        elif value < 2:
            value -= 1
            money_counter += 1
    return money_counter

any_number = int(input('Enter integer number: '))
result = amount_to_pay(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')



