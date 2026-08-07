items = ["name", "age", "name", "email", "age"]
result = []
seen = set()

for item in items:
    if item not in seen:
        result.append(item)
        seen.add(item)

print(result)

