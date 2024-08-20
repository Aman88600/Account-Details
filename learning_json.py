import json
f = open("data.json")
data = json.load(f)
for i in data:
    for j in data[i]:
    # print(f"{i} {data[i]}")
        print(f"key = {j} value = {data[i][j]}")
f.close()
