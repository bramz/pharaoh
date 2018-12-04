

class Player:
    def __init__(self, name):
        self.name = name
        self.stats = {
            'cash': 1000,
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


    def get_drug_quantity(self, drug) -> int:
        return int(self.drugs[drug])


    def get_weapon_quantity(self, weapon) -> int:
        return int(self.weapons[weapon])


    def receive_items(self, item: str, amount: int) -> str:
        if item in self.drugs:
            total = int(self.get_drug_quantity(item)) + amount
            self.drugs[item] = total
            return self.drugs[item]
        elif item in self.weapons:
            total = int(self.get_weapon_quantity(item)) + amount
            self.weapons[item] = total
            return self.weapons[item]


    def update_cash(self, amount: int, operation: str) -> str:
        cash = self.get_cash()
        if operation == "add":
            new_cash = int(cash) + int(amount)
            self.stats['cash'] = new_cash
        elif operation == "sub":
            new_cash = int(cash) - int(amount)
            self.stats['cash'] = new_cash


def create_player(name) -> Player:
    player = Player(name)
    return player
