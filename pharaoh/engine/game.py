import player.identity

""" Game Handlers """

def start_sequence():
    gender = player.identity.receive_gender()
    name = player.identity.receive_name()

    global ident
    ident = player.identity.establish_ident(gender, name)

    engine_loop()


def engine_loop():
    handle_sequences()


def handle_sequences():
    print("Welcome, " + ident.name)