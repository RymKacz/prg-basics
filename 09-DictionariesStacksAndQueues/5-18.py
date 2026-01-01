import json

with open('dogs.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
# `dogs.json` contains a list of dog dictionaries. Iterate over items.
for dog in data:
    age = dog.get('age')
    if  age < 5:
        # print name and age for clarity
        print(dog.get('name', 'unknown'), ':', age)