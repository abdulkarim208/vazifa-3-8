import json

with open("1_masala/user.json", "r") as f:
    data = json.load(f)

print(f"Ism: {data['ism']}, Yosh: {data['yosh']}")
print(f"Shahar: {data['shahar']}")