# ui.py

from tkinter import *
from tkinter import messagebox
from game import check_winner, is_draw, EMPTY, PLAYER_X, PLAYER_O

class TicTacToeUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tres en línea")

        self.board = [EMPTY] * 9
        self.buttons = []
        self.current_player = PLAYER_X

        self.create_board()
        self.create_menu()

    def create_board(self):
        for i in range(9):
            button = Button(
                self.root,
                text=EMPTY,
                font=("Helvetica", 20),
                height=3,
                width=6,
                command=lambda i=i: self.on_click(i)
            )
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def on_click(self, index):
        if self.board[index] != EMPTY:
            messagebox.showerror("Error", "La casilla ya está ocupada")
            return

        self.board[index] = self.current_player
        self.buttons[index].config(text=self.current_player)

        winner = check_winner(self.board)
        if winner:
            messagebox.showinfo("Fin del juego", f"{winner} es el ganador")
            self.disable_buttons()
            return

        if is_draw(self.board):
            messagebox.showinfo("Fin del juego", "Empate")
            self.disable_buttons()
            return

        self.switch_player()

    def switch_player(self):
        self.current_player = PLAYER_O if self.current_player == PLAYER_X else PLAYER_X

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state=DISABLED)

    def reset_game(self):
        self.board = [EMPTY] * 9
        self.current_player = PLAYER_X
        for button in self.buttons:
            button.config(text=EMPTY, state=NORMAL)

    def create_menu(self):
        menu = Menu(self.root)
        self.root.config(menu=menu)

        options = Menu(menu, tearoff=0)
        menu.add_cascade(label="Opciones", menu=options)
        options.add_command(label="Reiniciar", command=self.reset_game)