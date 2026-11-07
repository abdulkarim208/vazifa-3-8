jami = 0
eng_katta = 0
soni = 0

with open("9_masala/expenses.csv", "r") as file:
    data = file.readlines()

for qator in data[1:]:
    malumot = qator.split(",")
    summa = int(malumot[1])

    jami += summa
    soni += 1

    if summa > eng_katta:
        eng_katta = summa

print("Jami:", jami)
print("Eng katta:", eng_katta)
print("Soni:", soni)