from datetime import date

from Citizen import Citizen
from Passport import PassportId


ilya2 = Citizen("Ilya", "K", date.fromisoformat("1992-07-21"), PassportId(6715, 283910), "+79224783902", "ilya2")
ilya1 = Citizen("Ilya", "K", date.fromisoformat("1992-07-21"), PassportId(6715, 283910), "+79224783902", "ilya1")
ilya3 = Citizen("Ilya", "K", date.fromisoformat("1999-07-21"), PassportId(6715, 283911), "+79224783912")
petr = Citizen("Petr", "M", date.fromisoformat("1992-01-21"), PassportId(6715, 282110), "+79224343902")

unique_citizens = set()

unique_citizens.add(ilya2)
unique_citizens.add(ilya1)
unique_citizens.add(ilya3)
unique_citizens.add(petr)

print(unique_citizens)

ilya1.greet()
petr.greet()
