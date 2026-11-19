def f(dice):
    dice = str(dice)
    max_len = 1
    current_len = 1
    max_digit = dice[0]
    for i in range(1, len(dice)):
        if dice[i] == dice[i-1]:
            current_len += 1
        else:
            if current_len > max_len:
                max_len = current_len
                max_digit = dice[i-1]
            current_len = 1
    if current_len > max_len:
        max_digit = dice[-1]
    return int(max_digit)
if __name__ == "__main__":
    print(f("5233165554211"))
    print(f("2133"))
