import os
from random import randint

class Player:
    def __init__(self, HP):
        self.name = str
        self.HP = int
        self.ATK = int
        self.DEF = int

class Classes(Player):
    def __init__(self, name=str, level=int, HP=int, ATK=int, DEF=int):
        self.name = name
        self.level = level
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF

class Enemy(Classes):
    def __init__(self, name=str, level=int, HP=int, ATK=int, DEF=int):
        self.name = name
        self.level = level
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF

class App(Classes):
    def battle(self, a, b):
        while a >= 0 and b >= 0:
            print()
            input("# ")
        
    def enemy_choice(self):
        c = randint(1,3)
        if c == 1:
            return self.spider.name
        elif c == 2:
            return self.rat.name
        elif c == 3:
            return self.dog.name

    def draw(self):
        print("Xx"+40*"-"+"xX")

    def clear(self):
        os.system("cls")

    def save(self):
        list = [
            self.name,
            str(self.classe.level),
            str(self.classe.HP),
            str(self.classe.ATK),
            str(self.classe.DEF)
        ]

        self.f = open("load.txt", "w")

        for item in list:
            self.f.write(item + "\n")
        self.f.close()

    def playing(self):
        self.clear()
        r = self.enemy_choice()
        print(f"You will fight with: {r}")
        input("# ")

    def create_new(self):
        self.clear()
        self.name = input("Write your name: ")
        print(f"Welcome to the Coliseum, {self.name}!")
        self.draw()
        print("Choose your class:")
        print("(1) Warrior - HP = 10 | ATK = 6  | DEF = 4")
        print("(2) Mage    - HP = 6  | ATK = 12 | DEF = 2")
        print("(3) Ranger  - HP = 8  | ATK = 6  | DEF = 6")

        r = input("# ")

        if r == "1":
            self.classe = Classes("Warrior", 1, 10, 6, 4)
            self.new = False
            self.play = True
        
        elif r == "2":
            self.classe = Classes("Mage", 1, 6, 12, 2)
            self.new = False
            self.play = True

        elif r == "3":
            self.classe = Classes("Ranger", 1, 8, 6, 6)
            self.new = False
            self.play = True

        else:
            print("Unknow command.")

    def menu_show(self):
        self.clear()
        print("1, New Game")
        print("2, Load Game")
        print("3, Quit Game")
        
        r = input("# ")

        if r == "1":
            self.menu = False
            self.new = True

        elif r == "2":
            self.f = open("load.txt", "r")
            self.load_list = self.f.readlines()
            self.name = self.load_list[0][:-1]
            self.level = self.load_list[1][:-1]
            self.classe.HP = self.load_list[2][:-1]
            self.classe.ATK = self.load_list[3][:-1]
            self.classe.DEF = self.load_list[4][:-1]

            print(self.name, self.classe.HP, self.classe.ATK, self.classe.DEF)
            input("# ")

        elif r == "3":
            quit()

        else:
            print("Unknow command.")

    def __init__(self):
        self.run = True
        self.new = False
        self.menu = True
        self.play = False
        self.key = False

        # Enemy's list
        self.spider = Classes("Spider", 1, 4, 2, 1)
        self.rat = Classes("Rat", 1, 2, 1, 1)
        self.dog = Classes("Dog", 1, 8, 4, 2)

        self.c = None

        while self.run:

            while self.menu:
                self.menu_show()

            while self.new:
                self.create_new()

            while self.play:
                self.save()
                self.playing()

                self.r = input("# ")

                if self.r == "0":
                    self.play = False
                    self.menu = True
        
if __name__ == "__main__":
    app = App()
