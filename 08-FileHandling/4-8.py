import re

try:
    with open('files.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        
    # Matches a dot followed by exactly 4 characters at the end of the string/line
    matches = re.findall(r'^.*\.[a-zA-Z0-9]{4}$', content, re.MULTILINE)
    
    for match in matches:
        print(match)
except FileNotFoundError:
    print("File 'files.txt' not found.")
