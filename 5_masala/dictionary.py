import json

talaba = {
    "ism": "Sardor",
    "yosh": 20,
    "kurs": 2
}

matn = json.dumps(talaba)

print(matn)

data = json.loads(matn)

print(f"Talabaning ismi: {data['ism']}")