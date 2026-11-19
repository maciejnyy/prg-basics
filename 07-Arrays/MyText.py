def word_count(text):
    return len(text.split())

def sort_by_length(text):
    return sorted(text.split(), key=len, reverse=True)

def sort_alphabetically(text):
    return sorted(text.split(), key=str.lower)
