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
