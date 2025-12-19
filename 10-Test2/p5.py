import re
def f(first_letter, last_letter):
    pattern = rf'\b{first_letter}[a-zA-Z]*{last_letter}\b'
    with open('data.txt') as file:
        content = file.read()

    words = re.findall(pattern, content)
    return len(words)

print(f("w","d"))