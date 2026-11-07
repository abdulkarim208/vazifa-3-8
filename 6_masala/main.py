import csv

with open("6_masala/students.csv", "r") as f:
    data = csv.DictReader(f)

    for talaba in data:
        print(talaba["ism"])

        if int(talaba["yosh"]) > 20:
            print(f"20 yoshdan katta: {talaba['ism']}")