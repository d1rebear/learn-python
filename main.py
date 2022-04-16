from datetime import date


class PassportId:
    series: int
    number: int

    def __init__(self, series, number):
        self.series = series
        self.number = number

    def __str__(self):
        return f"{self.series} {self.number}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, PassportId):
            return False
        return (self.series == other.series
                and self.number == other.number)

    def __hash__(self):
        _hash = hash((self.series, self.number))
        print(f"PassportId.__hash__: {_hash}")
        return _hash


class Citizen:
    name: str
    surname: str
    birth_date: date
    passport_id: PassportId
    phone_number: str
    nuance: str

    def __init__(self, name, surname, birth_date, passport_id, phone_number, nuance="-"):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.passport_id = passport_id
        self.phone_number = phone_number
        self.nuance = nuance

    def __str__(self):
        return f"{self.name} {self.surname}" \
               f"\nborn {self.birth_date.strftime('%d.%m.%Y')}" \
               f"\npassport: {self.passport_id}" \
               f"\nphone: {self.phone_number}" \
               f"\nnuance: {self.nuance}"

    def __repr__(self):
        return f"{self.name} {self.surname}" \
               f" | born {self.birth_date.strftime('%d.%m.%Y')}" \
               f" | passport: {self.passport_id}" \
               f" | phone: {self.phone_number}" \
               f" | nuance: {self.nuance}"

    def __eq__(self, other):
        if not isinstance(other, Citizen):
            return False
        return (self.name == other.name
                and self.surname == other.surname
                and self.birth_date == other.birth_date
                and self.passport_id == other.passport_id
                and self.phone_number == other.phone_number)

    def __hash__(self):
        _hash = hash((self.name, self.surname, self.birth_date, self.passport_id, self.phone_number))
        print(f"Citizen.__hash__: {_hash}")
        return _hash

    def greet(self):
        print(f"Hello! I am {self.name} {self.surname}")


ilya2 = Citizen("Ilya", "K", date.fromisoformat("1992-07-21"), PassportId(6715, 283910), "+79224783902", "ilya2")
ilya1 = Citizen("Ilya", "K", date.fromisoformat("1992-07-21"), PassportId(6715, 283910), "+79224783902", "ilya1")
ilya3 = Citizen("Ilya", "K", date.fromisoformat("1999-07-21"), PassportId(6715, 283911), "+79224783912")
petr = Citizen("Petr", "M", date.fromisoformat("1992-01-21"), PassportId(6715, 282110), "+79224343902")

unique_citizens = set()

unique_citizens.add(ilya2)
unique_citizens.add(ilya1)
unique_citizens.add(ilya3)
unique_citizens.add(petr)
unique_citizens.add(petr)

print(unique_citizens)

ilya1.greet()
petr.greet()
