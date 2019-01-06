import player.identity


""" Game Handlers """

def start_sequence(screen):
    gender = player.identity.receive_gender(screen)
    name = player.identity.receive_name(screen)

    global ident
    ident = player.identity.establish_ident(gender, name)

    engine_loop()


def engine_loop():
    handle_sequences()


def handle_sequences():
    print("Welcome, " + ident.name)
