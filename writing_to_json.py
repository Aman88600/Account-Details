import json
# file = open("data.json")
data = {"Name" : "Aman Basoya", "Age" : 21}
# file.write(x)
# file.close()

with open("data.json", "w") as fp:
    json.dump(data, fp, indent=6)