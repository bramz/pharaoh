import player.identity


""" Game Handlers """

def start_sequence(screen):
    engine_loop()


def engine_loop():
    handle_sequences()


def handle_sequences():
    gender = player.identity.receive_gender(screen)
    name = player.identity.receive_name(screen)
    ident = player.identity.establish_ident(gender, name)
    print("Welcome, " + ident.name)
