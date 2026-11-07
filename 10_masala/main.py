with open("10_masala/sportchilar.csv", "r") as file:
    data = file.readlines()

for qator in data[1:]:
    malumot = qator.strip().split(",")

    ism = malumot[0]
    sport = malumot[1]
    ball = int(malumot[2])

    print(ism, sport, ball)

print("\n80 balldan yuqori sportchilar:")

for qator in data[1:]:
    malumot = qator.strip().split(",")
    ball = int(malumot[2])

    if ball > 80:
        print(malumot[0], ball)

eng_katta = 0

for qator in data[1:]:
    malumot = qator.strip().split(",")
    ball = int(malumot[2])

    if ball > eng_katta:
        eng_katta = ball
        eng_yaxshi = malumot[0]

print("\nEng yuqori ball:", eng_yaxshi, eng_katta)