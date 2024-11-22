import json

json_file = "ex_2_edited.json"

with open(json_file) as file:
    data = json.load(file)
    phone_dict = {}
    for user in data["users"]:
        phone_dict[user["name"]] = user["phoneNumber"]

    print(phone_dict)
