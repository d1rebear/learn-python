from datetime import date
from Passport import PassportId


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
