import re

text = input("Enter text: ")
vowels = re.findall(r'[aeiouAEIOU]', text)
print(f"Number of vowels: {len(vowels)}")
