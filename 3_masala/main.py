import json

with open("3_masala/student.json", "r") as f:
    data = json.load(f)

data["ball"] = 95

with open("3_masala/new_student.json", "w") as f:
    json.dump(data, f, indent=4)
print("saqlandi")