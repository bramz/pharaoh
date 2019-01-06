""" Player Identity """

class Identity:
    def __init__(self, gender: str, name: str):
        self.gender = gender
        self.name = name

    def gender(self) -> str:
        return self.gender

    def name(self) -> str:
        return self.name


def receive_gender() -> str:
    gender = input("What is your gender? ")
    return gender


def receive_name() -> str:
    name = input("What is your name? ")
    return name


def establish_ident(gender: str, name: str) -> Identity:
    ident = Identity(gender, name)
    return ident
