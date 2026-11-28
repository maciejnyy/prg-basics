translations = {
    'computer': 'komputer',
    'mouse': 'myszka',
    'keyboard': 'klawiatura',
    'printer': 'drukarka'
}

word = input("Enter an English word: ").lower()
if word in translations:
    print(f"Polish translation: {translations[word]}")
else:
    print("Translation is unavailable.")
