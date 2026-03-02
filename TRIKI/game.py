# game.py

EMPTY = " "
PLAYER_X = "X"
PLAYER_O = "O"

WIN_COMBINATIONS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # filas
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columnas
    (0, 4, 8), (2, 4, 6)              # diagonales
]

def check_winner(board):
    for a, b, c in WIN_COMBINATIONS:
        if board[a] == board[b] == board[c] != EMPTY:
            return board[a]
    return None

def is_draw(board):
    return EMPTY not in board

def valid_moves(board):
    return [i for i, cell in enumerate(board) if cell == EMPTY]