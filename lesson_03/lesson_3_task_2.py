from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15", "+79991112233"),
    Smartphone("Samsung", "Galaxy S24", "+79994445566"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79997778899"),
    Smartphone("Google", "Pixel 8", "+79990001122"),
    Smartphone("Huawei", "P60 Pro", "+79993334455")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
