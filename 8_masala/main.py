ism = input("Ism kiriting: ")
yosh = input("Yosh kiriting: ")
kurs = input("Kurs kiriting: ")

with open("8_masala/students.csv", "a") as file:
    file.write(f"\n{ism},{yosh},{kurs}")

with open("8_masala/students.csv", "r") as file:
    data = file.read()
    print(data)