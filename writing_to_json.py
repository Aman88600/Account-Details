import json


number_of_details = int(input("How many details you want to enter"))
details = {}
i = 0
while i < number_of_details:
    detail_name = str(input("Enter Detail Name : "))
    detail_data = input("Enter Detail Data : ")
    details[detail_name] = detail_data
    i += 1
print(details)
# name = str(input("Enter your Name :"))
# age = int(input("Enter your Age : "))

# data = {"Name" : name, "Age" : age}
with open("data.json", "w") as fp:
    json.dump(details, fp, indent=4)