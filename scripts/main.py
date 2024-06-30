import os
from time import sleep
from random import randint
from data import *

class Pokemon:
    def take_damage(self, target):
        self.target = target

    def __init__(self,
                 name,
                 type1,
                 type2,
                 level,
                 current_exp,
                 next_lvl):
        #Basic stats
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.level = level

        self.sex_chance = randint(1,2)
        if self.sex_chance == 1:
            self.sex = SEX[0]
        elif self.sex_chance == 2:
            self.sex = SEX[1]

        #Advanced stats
        self.hp = int
        self.max_hp = int
        self.current_exp = current_exp
        self.next_lvl = next_lvl

        #Battle stats
        self.attack = int
        self.special_atk = int
        self.defense = int
        self.special_def = int
        self.speed = int

        self.ID = randint(1, 9999)

class Pokemon_index(Pokemon):
    def __init__(self):
        self.pokemons = []


class Trainer:
    def level_up(self):
        pass

    def __init__(self):
        self.name = str
        self.level = int
        self.exp = int

        self.pokemons_owned = []

        if len(self.pokemons_owned) == 6:
            pass

class App:
    def save(self):
        list = [
            self.trainer.name,
            self.trainer.level,
            self.trainer.exp,

        ]

        self.f = open("load.txt", "w")

        for item in list:
            self.f.write(item + "\n")
        self.f.close()
    
    def draw(self):
        print("Xx" + 40*"-" + "xX")

    def clear(self):
        os.system("cls")

    def fight(self):
        self.rival = Trainer()
        self.rival.name = OTHER_TRAINERS[0]["name"]

        print(f"{self.trainer.name}, you will fight VS {self.rival.name}!")
        input("> ")

    def pause_menu_show(self):
        print("(1) Continue")
        print("(2) Save")
        print("(3) Quit")

        r = input("> ")

        if r == "1":
            pass
        elif r == "2":
            pass
        elif r == "3":
            pass
        else:
            print("Unknow command.")
            input("> ")

    def create_new(self):
        self.trainer.level = 1
        self.trainer.exp = 0
        self.clear()
        self.draw()
        print("Choose one of the starters: ")
        print("(1) Bulbasaur")
        print("(2) Charmander")
        print("(3) Squirtle")
        r = input("> ")

        if r == "1":
            self.starter = Pokemon(POKEMONS[0],
                                   ELEMENT_TYPES[11],
                                   ELEMENT_TYPES[3],
                                   5,
                                   0,
                                   100)
            self.trainer.pokemons_owned.append(POKEMONS[0])
            self.c = False
            self.new = False
            self.playing = True

        elif r == "2":
            self.trainer.pokemons_owned.append(POKEMONS[1])
            self.c = False
            self.new = False
            self.playing = True

        elif r == "3":
            self.trainer.pokemons_owned.append(POKEMONS[2])
            self.c = False
            self.new = False
            self.playing = True

        else:
            print("Unknow command.")
            sleep(1)
    
    def play(self):
        self.clear()
        print("Loading...")
        print(self.trainer.pokemons_owned)
        input("> ")
        self.playing = False
        self.battle = True

    def menu_show(self):
        self.clear()
        self.draw()
        print("(1) New Game")
        print("(2) Load Game")
        print("(3) Exit")
        r = input("> ")

        if r == "1":
            self.menu = False
            self.new = True

        if r == "2":
            pass

        if r == "3":
            quit()

        else:
            print("Unknow command.")

    def __init__(self):
        self.run = True
        self.pause_menu = False
        self.menu = True
        self.new = False
        self.playing = False
        self.battle = False

        self.trainer = Trainer()

        self.c = True

        while self.run:
            while self.battle:
                self.fight()

            while self.pause_menu:
                self.pause_menu_show()

            while self.menu:
                self.menu_show()

            while self.new:
                self.clear()
                self.draw()
                print("What's your name, trainer?")
                self.trainer.name = input("> ")
                print(f"Welcome to the world Pokemon, {self.trainer.name.capitalize()}!")
                sleep(2)

                while self.c:
                    self.create_new()

            while self.playing:
                self.play()

                self.c = input("# ")

                if self.c == "0":
                    self.play = False
                    self.pause_menu = True

if __name__ == "__main__":
    app = App()
