import MyText

text = "An apple a day keeps the doctor away"
print(f"Text: {text}")
print(f"Number of words: {MyText.word_count(text)}")
print(f"Words from the longest: {','.join(MyText.sort_by_length(text))}")
print(f"Words ordered alphabetically: {','.join(MyText.sort_alphabetically(text))}")
