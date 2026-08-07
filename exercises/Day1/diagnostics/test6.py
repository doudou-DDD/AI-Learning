fields = [
    {'name': 'username', 'type': 'string', 'required': True},
    {'name': 'age', 'type': 'integer', 'required': False},
    {'name': 'email', 'type': 'string', 'required': True},
]

required_fields = [field['name'] for field in fields if field['required']]

with open('fields.json', 'w', encoding='utf-8') as f:
    json.dump(fields, f, ensure_ascii=False, indent=2)

with open('fields.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(required_fields)
print(data)

