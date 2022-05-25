import random
from math import inf
from piece import *

def random_move(board):
    """
    Selects a random move from the valid moves for the current players turn
    :param board: the current board being used for the game (Board)
    :return: tuple representing move; format: ((sourceX, sourceY), (destX, destY))
    """
    moves = board.get_moves()
    if moves:
        return random.choice(moves)


def evaluate(board, maximizing_color):
        if maximizing_color == WHITE:
            return board.whiteScore + board.score_position()[1] - board.blackScore - board.score_position()[0]
        else:
            return board.blackScore + board.score_position()[0] - board.whiteScore - board.score_position()[1]


""" def minimax(board, depth, maximizing_player, maximizing_color):
    if depth == 0 or board.gameover:
        return None, evaluate(board, maximizing_color)
    moves = board.get_moves()
    best_move = random.choice(moves)

    if maximizing_player:
        max_eval = -inf
        for move in moves:
            board.make_move(move[0], move[1])
            current_eval = minimax(board, depth - 1, False, maximizing_color)[1]
            board.unmake_move()
            if current_eval > max_eval:
                max_eval = current_eval
                best_move = move
        return best_move, max_eval
    else:
        min_eval = inf
        for move in moves:
            board.make_move(move[0], move[1])
            current_eval = minimax(board, depth - 1, True, maximizing_color)[1]
            board.unmake_move()
            if current_eval < min_eval:
                min_eval = current_eval
                best_move = move
        return best_move, min_eval """
def minimax(board, depth, alpha, beta, maximizing_player, maximizing_color):
   if depth == 0 or board.gameover:
       return None, evaluate(board, maximizing_color)
   moves = board.get_moves()
   best_move = random.choice(moves)


   if maximizing_player:
       max_eval = -inf
       for move in moves:
           board.make_move(move[0], move[1])
           current_eval = minimax(board, depth - 1, alpha, beta, False, maximizing_color)[1]
           board.unmake_move()
           if current_eval > max_eval:
               max_eval = current_eval
               best_move = move
           alpha = max(alpha, current_eval)
           if beta <= alpha:
               break
       return best_move, max_eval
   else:
       min_eval = inf
       for move in moves:
           board.make_move(move[0], move[1])
           current_eval = minimax(board, depth - 1, alpha, beta, True, maximizing_color)[1]
           board.unmake_move()
           if current_eval < min_eval:
               min_eval = current_eval
               best_move = move
           beta = min(beta, current_eval)
           if beta <= alpha:
               break
       return best_move, min_eval


