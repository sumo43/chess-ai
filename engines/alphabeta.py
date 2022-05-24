import chess
from util import naive_eval_function
import json

EVAL_FUNC = naive_eval_function
MAX_DEPTH = 2

memo = None


def alphabeta_algorithm(board, depth, alpha, beta, maximizing_player):
    board_value = naive_eval_function(board)
    if depth == 0 or abs(board_value) == 200:
        return board_value

    if maximizing_player:
        value = -9999
        for child in board.legal_moves:
            board.push(child)
            value = max(value, alphabeta_algorithm(board, depth - 1,
                        alpha, beta, not maximizing_player))
            board.pop()
            if value >= beta:
                break
            a = max(alpha, value)
        return value
    else:
        value = 9999
        for child in board.legal_moves:
            board.push(child)
            value = min(value, alphabeta_algorithm(board, depth - 1,
                        alpha, beta, not maximizing_player))
            board.pop()
            # we dont have to search any further, since this move is already less than alpha (for max player)
            if value <= alpha:
                break
            # but this move might be less than alpha, which we can use
            a = min(alpha, value)
        return value


def alphabeta(board, maximizing_player, depth=MAX_DEPTH):

    # the minimum score that the maximizing player is assured of
    alpha = -9999

    # the maximum score that the minimizing player is assured of
    beta = 9999

    # same thing as alphabeta, but this time we want the move instead of value

    if maximizing_player:
        value = -9999
        move = None
        for child in board.legal_moves:
            board.push(child)
            child_value = alphabeta_algorithm(board, depth - 1,
                                              alpha, beta, not maximizing_player)
            if child_value > value:
                value = child_value
                move = child
            board.pop()
            if value >= beta:
                break
            a = max(alpha, value)
        return move
    else:
        value = 9999
        move = None
        for child in board.legal_moves:
            board.push(child)
            child_value = alphabeta_algorithm(board, depth - 1,
                                              alpha, beta, not maximizing_player)
            if child_value < value:
                value = child_value
                move = child
            board.pop()
            # we dont have to search any further, since this move is already less than alpha (for max player)
            if value <= alpha:
                break
            # but this move might be less than alpha, which we can use
            a = min(alpha, value)
        return move


if __name__ == "__main__":

    print("Starting pos:")
    board = chess.Board()
    print(board)
    print()

    while not board.is_variant_win() and not board.is_variant_loss():

        print("Current turn: ")
        print("WHITE" if board.turn else "BLACK")
        print()
        print(board)
        print('a|b|c|d|e|f|g|h')
        print()

        if board.turn:
            user_move = input()
            move = chess.Move.from_uci(user_move)

            while move not in board.legal_moves:
                print("Invalid move, try again...")

                user_move = input()
                move = chess.Move.from_uci(user_move)

            board.push(move)
        else:
            ai_move = alphabeta(board, SEARCH_DEPTH)
            board.push(ai_move)

    turn = "WHITE" if board.turn else "BLACK"
    print(turn + " won")

