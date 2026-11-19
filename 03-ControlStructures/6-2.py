text = "This is a sample text"
vowels = "aeiouAEIOU"
count = 0
i = 0
while i < len(text):
    if text[i] in vowels: count += 1
    i += 1
print(f"Vowels: {count}")
