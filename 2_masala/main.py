import json

with open("2_masala/product.json", "r") as f:
    data = json.load(f)

jami = data["narx"] * data["miqdor"]

print(f"Mahsulot: {data['nom']}")
print(f"Umumiy qiymati: {jami}")