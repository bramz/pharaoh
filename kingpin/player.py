

class Player:
    def __init__(self, name):
        self.name = name
        self.stats = {
            'cash': 1001,
            'properties': 1,
            'cars': 0,
            'rank': 0,
        }

        self.drugs = {
            'cannabis': 1,
            'cocaine': 0,
            'heroin': 0,
        }

        self.weapons = {
            'pistol': 1,
            'rifle': 0,
            'shotgun': 0,
            'sniper': 0,
            'explosives': 0,
        }


    def get_stats(self) -> dict:
        return self.stats

    
    def get_drugs(self) -> dict:
        return self.drugs

    
    def get_weapons(self) -> dict:
        return self.weapons


    def get_cash(self) -> str:
        return self.stats['cash']

    
    def get_properties(self) -> int:
        return self.stats['properties']


    def get_cars(self) -> int:
        return self.stats['cars']


    def get_rank(self) -> int:
        return self.stats['rank']


    def get_drug_quantity(self, drug) -> int:
        return int(self.drugs[drug])


    def get_weapon_quantity(self, weapon) -> int:
        return int(self.weapons[weapon])


    def update_items(self, item: str, amount: int, operation: str) -> None:
        if item in self.drugs:
            if operation == "add":
                total = int(self.get_drug_quantity(item)) + amount
                self.drugs[item] = total
            elif operation == "sub":
                total = int(self.get_drug_quantity(item)) - amount
                self.drugs[item] = total
        if item in self.weapons:
            if operation == "add":
                total = int(self.get_weapon_quantity(item)) + amount
                self.weapons[item] = total
            elif operation == "sub":
                total = int(self.get_weapon_quantity(item)) - amount
                self.weapons[item] = total


    def update_stats(self, amount: int, operation: str, stype: str) -> None:
        if stype == "cash":
            cash = self.get_cash()
            if operation == "add":
                new_cash = int(cash) + int(amount)
                self.stats[stype] = new_cash
            elif operation == "sub":
                new_cash = int(cash) - int(amount)
                self.stats[stype] = new_cash
        elif stype == "properties":
            prop = self.get_properties()
            if operation == "add":
                new_prop = int(prop) + int(amount)
                self.stats[stype] = new_prop
            elif operation == "sub":
                new_prop = int(prop) - int(amount)
                self.stats[stype] = new_prop
        elif stype == "cars":
            cars = self.get_cars()
            if operation == "add":
                new_cars = int(cars) + int(amount)
                self.stats[stype] = new_cars
            elif operation == "sub":
                new_cars = int(cars) - int(amount)
                self.stats[stype] = new_cars
        elif stype == "rank":
            rank = self.get_rank()
            if operation == "add":
                new_rank = int(rank) + int(amount)
                self.stats[stype] = new_rank
            elif operation == "sub":
                new_rank = int(rank) - int(amount)
                self.stats[stype] = new_rank


def create_player(name) -> Player:
    player = Player(name)
    return player
