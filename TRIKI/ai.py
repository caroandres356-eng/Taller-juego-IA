# ai.py

from game import check_winner, valid_moves, EMPTY, PLAYER_X, PLAYER_O
import math

def minimax(board, depth, is_maximizing, alpha, beta, ai_player):
    """
    Evalúa el tablero actual usando el algoritmo Minimax con poda Alfa-Beta.
    """
    human_player = PLAYER_X if ai_player == PLAYER_O else PLAYER_O
    winner = check_winner(board)
    
    # Casos base: alguien ganó o hay empate
    if winner == ai_player:
        return 10 - depth
    elif winner == human_player:
        return depth - 10
    elif not valid_moves(board):
        return 0
        
    if is_maximizing:
        max_eval = -math.inf
        for move in valid_moves(board):
            board[move] = ai_player
            eval = minimax(board, depth + 1, False, alpha, beta, ai_player)
            board[move] = EMPTY
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break # Poda Beta
        return max_eval
    else:
        min_eval = math.inf
        for move in valid_moves(board):
            board[move] = human_player
            eval = minimax(board, depth + 1, True, alpha, beta, ai_player)
            board[move] = EMPTY
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break # Poda Alfa
        return min_eval

def get_best_move(board, ai_player):
    """
    Devuelve la mejor jugada (índice 0-8) para la IA usando Minimax.
    """
    best_score = -math.inf
    best_move = None
    alpha = -math.inf
    beta = math.inf
    
    for move in valid_moves(board):
        board[move] = ai_player
        score = minimax(board, 0, False, alpha, beta, ai_player)
        board[move] = EMPTY
        
        if score > best_score:
            best_score = score
            best_move = move
            
    return best_move