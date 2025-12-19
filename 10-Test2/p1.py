import re
def f(player1, player2):
    high_values_pattern = '[AKQJT]' 
    value1 = 0
    value2 = 0
    for char in player1:
        char_match = bool(re.match(high_values_pattern,char))
        if char_match:
            value1 += 10
        else:
            value1 += int(char)
    for char in player2:
        char_match = bool(re.match(high_values_pattern,char))
        if char_match:
            value2 += 10
        else:
            value2 += int(char)
    if value1 >= value2:
        return True
    else:
        return False

print(f("9532","K8"))



