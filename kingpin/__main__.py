import sys
from game import start_game

arguments = list(sys.argv[2:])

def read_banner_file():
    try:
        with open('data/banner.txt', 'r') as fh:
            banner = fh.read()
            print(banner)     
    except IOError:
        pass

def handle_arguments(arguments):
    if len(arguments) >= 1:
        if arguments[0] == "start":
            start_game()
    else:
        print("Usage: python kingpin main start")

if __name__ == "__main__":
    read_banner_file()
    handle_arguments(arguments)


