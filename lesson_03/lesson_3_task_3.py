from address import Address
from mailing import Mailing

addr_to = Address("123456", "Москва", "Ленина", "10", "45")
addr_from = Address("654321", "Самара", "Ново-Садовая", "15", "12")

mail = Mailing(addr_to, addr_from, 350, "TRK987654321")

print(
    f"Отправление {mail.track} из {mail.from_address.index}, "
    f"{mail.from_address.city}, {mail.from_address.street}, "
    f"{mail.from_address.house} - {mail.from_address.apartment} "
    f"в {mail.to_address.index}, {mail.to_address.city}, "
    f"{mail.to_address.street}, {mail.to_address.house} - "
    f"{mail.to_address.apartment}. Стоимость {mail.cost} рублей."
)
