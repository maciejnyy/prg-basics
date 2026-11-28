import json

favourite = {
    "title": "Inception",
    "director": "Christopher Nolan",
    "year": 2010,
    "genre": ["Sci-Fi", "Action", "Thriller"],
    "rating": 8.8
}

with open('favourite.json', 'w', encoding='utf-8') as file:
    json.dump(favourite, file, indent=4)

print("Saved to favourite.json")
