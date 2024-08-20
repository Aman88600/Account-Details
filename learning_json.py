import json
f = open("data.json")
data = json.load(f)
for i in data:
    print(f"Key = {i} value = {data[i]}")
f.close()
