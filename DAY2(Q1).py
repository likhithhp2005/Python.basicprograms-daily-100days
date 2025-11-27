d = {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 20}

unique = {}
seen = set()

for k, v in d.items():
    if v not in seen:
        unique[k] = v
        seen.add(v)

print("Dictionary after removing duplicate values:", unique)