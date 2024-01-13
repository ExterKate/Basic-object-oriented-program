import tkinter as tk
from settings import *

class Game:
    def __init__(self, master):
        super().__init__()
        self.master = master
        centralized(self.master)
        self.master.title('Prince')
        self.master.resizable(False, False)

if __name__ == '__main__':
    root = tk.Tk()
    game = Game(root)
    root.mainloop()
