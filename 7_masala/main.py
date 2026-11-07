import csv

with open("7_masala/products.csv", "r") as f:
    data = csv.DictReader(f)

    eng_qimmat = 0
    nomi = ""

    for mahsulot in data:
        narx = int(mahsulot["narx"])
        miqdor = int(mahsulot["miqdor"])

        jami = narx * miqdor

        print(f"{mahsulot['nom']} — {jami}")

        if narx > eng_qimmat:
            eng_qimmat = narx
            nomi = mahsulot["nom"]

    print(f"Eng qimmat mahsulot: {nomi}")