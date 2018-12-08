

class Player:
    def __init__(self, name):
        self.name = name
        self.stats = {
            'cash': 2000,
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
            else:
                total = int(self.get_drug_quantity(item)) - amount
                self.drugs[item] = total
        if item in self.weapons:
            if operation == "add":
                total = int(self.get_weapon_quantity(item)) + amount
                self.weapons[item] = total
            else:
                total = int(self.get_weapon_quantity(item)) - amount
                self.weapons[item] = total


    def update_stat(self, stat: str, amount: int, operation: int) -> None:
        if stat not in self.stats:
            raise KeyError(f'unknown stat {stat}')
        
        if operation == "add":
            self.stats[stat] = self.stats[stat] + amount
        else:
            self.stats[stat] = self.stats[stat] - amount


    def update_rank(self):
        rank = self.calc_rank()
        self.stats['rank'] = rank


    def calc_rank(self) -> str:
        if self.stats['cash'] in range(0,10000):
            return 'soldato'
        elif self.stats['cash'] in range(10000,25000):
            return 'caporegime'
        elif self.stats['cash'] in range(25000, 50000):
            return 'consigliere'
        elif self.stats['cash'] in range(50000, 100000):
            return 'underboss'
        elif self.stats['cash'] in range(100000, 1000000):
            return 'kingpin'



def create_player(name) -> Player:
    player = Player(name)
    return player
