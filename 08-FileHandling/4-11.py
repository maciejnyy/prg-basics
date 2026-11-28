def write_powers():
    with open('powers.txt', 'w', encoding='utf-8') as file:
        for i in range(1, 101):
            line = f"{i},{i**2},{i**3}\n"
            print(line, end="")
            file.write(line)

if __name__ == "__main__":
    write_powers()
