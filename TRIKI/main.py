# main.py

from tkinter import Tk
from ui import TicTacToeUI

def main():
    root = Tk()
    app = TicTacToeUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()