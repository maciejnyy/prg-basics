person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming", "excursions"],
    "married": True,
    "phone": {"landline": "123444321", "mobile": "777888999"}
}

# 1. Displays name
print("Name:", person["name"])

# 2. Displays hobby
print("Hobby:", person["hobby"])

# 3. Displays the entire contents of the dictionary
print("Original dictionary:", person)

# 4. Changes surname to 'Nowak'
person["surname"] = "Nowak"

# 5. Changes person's marriage status
person["married"] = not person["married"]

# 6. Adds gender: 'male'
person["gender"] = "male"

# 7. Adds a new hobby: 'bicycle'
person["hobby"].append("bicycle")

# 8. Adds work phone to existing phones: '313131444'
person["phone"]["work"] = "313131444"

# 9. Displays the entire contents of the dictionary (iterate over dictionary items)
print("\nUpdated dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")
