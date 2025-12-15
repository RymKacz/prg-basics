import json
candidats = {}
try:
    with open ('votes.json', 'r', encoding='utf-8') as f:
        content = f.read()
        if content:
            candidats = json.loads(content)
except FileNotFoundError:
    pass
person_name = input('Name of the person you are voting for:')
candidats[person_name] = candidats.get(person_name, 0) + 1
with open ('votes.json', 'w', encoding='utf-8') as f:
    json.dump(candidats, f, ensure_ascii=False)