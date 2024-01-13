BG = "#191818"
FG = "#d4c8bb"
FONT = "times"
FS = 20

IMGX = 32
IMGY = 32

def centralized(master):
    WIDTH = 800 #janela.winfo_reqwidth()
    HEIGHT = 600 #janela.winfo_reqheight()

    largura = master.winfo_screenwidth()
    altura = master.winfo_screenheight()

    x = (largura - WIDTH) // 2
    y = (altura - HEIGHT) // 2

    master.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")