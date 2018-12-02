# user package

class Player:
    def __init__(self, name):
        self.name = name
        self.stats = {
            'Cash': 250,
            'Properties': 1,
            'Cars': 0,
            'Rank': 0,
        }

        self.drugs = {
            'Cannabis': 1,
            'Cocaine': 0,
            'Heroin': 0,
        }

        self.weapons = {
            'Pistols': 1,
            'Rifles': 0,
            'Shotguns': 0,
            'Snipers': 0,
            'Explosives': 0,
        }


    def get_stats(self) -> str:
        return self.stats

    
    def get_drugs(self) -> dict:
        return self.drugs

    
    def get_weapons(self) -> dict:
        return self.weapons


def create_player(name) -> Player:
    player = Player(name)
    return player
