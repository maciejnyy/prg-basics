import json
import os

file_name = 'voting.json'

if os.path.exists(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        votes = json.load(file)
else:
    votes = {}

person_name = input('Name of the person you are voting for: ')
votes[person_name] = votes.get(person_name, 0) + 1

with open(file_name, 'w', encoding='utf-8') as file:
    json.dump(votes, file, indent=4)

print("Updated voting results:", votes)
