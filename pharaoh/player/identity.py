from pygame.locals import *
import pygame, string
import lib.inputs

""" Player Identity """

class Identity:
    def __init__(self, gender: str, name: str):
        self.gender = gender
        self.name = name

    def gender(self) -> str:
        return self.gender

    def name(self) -> str:
        return self.name


def receive_gender(screen) -> str:
    gender = ''
    lib.inputs.input_box(screen, "What is your gender? " + gender)
    return gender


def receive_name(screen) -> str:
    name = ''
    lib.inputs.input_box(screen, "What is your name? " + name)
    return name


def establish_ident(gender: str, name: str) -> Identity:
    ident = Identity(gender, name)
    return ident
