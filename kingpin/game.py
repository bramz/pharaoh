import asyncio
import random
from player import create_player


def start_game():
    name = input("What is your name? ")
    print('Starting game as %s' % name)
 
    global player
    player = create_player(name)
 
    turn_loop()


def turn_loop():
    while True:
        handle_action()    


def handle_action():
    action = input("Enter an action (buy/sell/travel/stats): ")

    if action == "buy":
        handle_buying()
    elif action == "sell":
        handle_sales()
    elif action == "travel":
        handle_travel()
    elif action == "stats":
        stats = player.get_stats()
        print(stats)
                

def list_drugs() -> dict:
    drugs_list = {
        'Cannabis': random_price(100, 1001),
        'Cocaine': random_price(1000, 10001),
        'Heroin': random_price(10000, 30001),
    }
    return drugs_list


def list_weapons() -> dict:
    weapons_list = {
        'Pistol': random_price(100, 1001),
        'Rifle': random_price(1000, 10001),
        'Shotgun': random_price(1000, 10001),
        'Sniper': random_price(5000, 20001),
        'Explosives': random_price(10000, 50001),
    }
    return weapons_list


def handle_buying():
    purchase_type  = input("What will you buy (drugs/weapons) ? ")
    if purchase_type == "drugs":
        print(list_drugs())
        drug_type = input("What type of drugs? ")
    elif purchase_type == "weapons":
        print(list_weapons())


def handle_sales():
    stats = player.get_stats()
    print(stats)


def handle_travel():
    stats = player.get_stats()
    print(stats)


def random_price(price_rangex, price_rangey) -> str:
    return "$%i" % random.randint(price_rangex, price_rangey)

