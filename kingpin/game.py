import random
from player import create_player
from items import *


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
    action = input("Enter an action (buy/sell/stats): ")

    if action == "buy":
        buying_items(purchase_type())
    elif action == "sell":
        selling_items(purchase_type())
    elif action == "stats":
        player.update_rank()
        print("\n{player} stats:".format(player=player.name))
        print("{stats}\n{drugs}\n{weapons}\n".format(
            stats=player.get_stats(), 
            drugs=player.get_drugs(), 
            weapons=player.get_weapons()
            )
        )


def list_drugs() -> dict:
    drugs_list = {
        'cannabis': random_price(100, 1001),
        'cocaine': random_price(1000, 10001),
        'heroin': random_price(10000, 20001),
    }
    return drugs_list


def list_weapons() -> dict:
    weapons_list = {
        'pistol': random_price(100, 1001),
        'rifle': random_price(1000, 10001),
        'shotgun': random_price(1000, 10001),
        'sniper': random_price(5000, 20001),
        'explosives': random_price(10000, 50001),
    }
    return weapons_list


def purchase_type() -> str:
    ptype = input("What will you buy or sell (drugs/weapons)? ")
    return ptype


def item_type() -> str:
    dtype = input("What type? ")
    return dtype


def receive_units() -> int:
    quantity = input("How many units? ")
    return quantity

    
def buying_items(ptype: str):
    if ptype == "drugs":
        dlist = list_drugs()
        print(dlist)

        itype = item_type()
        player_cash = player.get_cash()
        price = dlist[itype][1:]
        quantity = receive_units()
        total_cost = determine_total_cost(int(price), int(quantity))
        print(check_buy_total(quantity, itype, price, total_cost, player_cash))
    elif ptype == "weapons":
        wlist = list_weapons()
        print(wlist)

        itype = item_type()
        player_cash = player.get_cash()
        price = wlist[itype][1:]
        quantity = receive_units()
        total_cost = determine_total_cost(int(price), int(quantity))
        print(check_buy_total(quantity, itype, price, total_cost, player_cash))

        
def selling_items(ptype: str):
    if ptype == "drugs":
        dlist = list_drugs()
        print(dlist)
        
        itype = item_type()
        player_total = player.drugs[itype]
        price = dlist[itype][1:]
        quantity = receive_units()
        total_cost = determine_total_cost(int(price), int(quantity))
        print(check_sales_total(quantity, itype, price, total_cost, player_total))
    elif ptype == "weapons":
        wlist = list_weapons()
        print(wlist)

        itype = item_type()
        player_total = player.weapons[itype]
        price = wlist[itype][1:]
        quantity = receive_units()
        total_cost = determine_total_cost(int(price), int(quantity))
        print(check_sales_total(quantity, itype, price, total_cost, player_total))


def check_buy_total(quantity: int, item: str, price: int, total_cost: int, player_cash: int) -> str:
    if int(total_cost) <= int(player_cash):
        player.update_items(item, int(quantity), "add")
        player.update_stat("cash", total_cost, "sub")
        return "Purchasing {quantity} units of {item} at ${price} for ${total_cost}".format(quantity=quantity, price=price, total_cost=total_cost, item=item)
    else:
        return "You do not have enough money."


def check_sales_total(quantity: int, item: str, price: int, total_cost: int, player_total: int) ->str:
    if int(quantity) <= int(player_total):
        player.update_items(item, int(quantity), "sub")
        player.update_stat("cash", total_cost, "add")
        return "Selling {quantity} units of {item} at ${price} for ${total_cost}".format(quantity=quantity, item=item, price=price, total_cost=total_cost)
    else:
        return "You do not have {quantity} units of {item}".format(quantity=quantity, item=item)


def random_price(price_rangex, price_rangey) -> str:
    return "$%i" % random.randint(price_rangex, price_rangey)


def determine_total_cost(price: int, quantity: int) -> int:
    total = price * quantity
    return total
