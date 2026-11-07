import json

with open("4_masala/phone.json", "r") as f:
    data = json.load(f)

print(f"Telefon modeli: {data['model']}")

yangi_narx = int(input("Yangi narxni kiriting: "))

data["narx"] = yangi_narx

with open("4_masala/new_phone.json", "w") as f:
    json.dump(data, f, indent=4)
print("yangi malumot saqlandi!")