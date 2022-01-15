import chess
from util import naive_eval_function

SEARCH_DEPTH = 6
eval_function = naive_eval_function


def min(board, depth, alpha, beta, moves):

    if(depth == 0):
        return eval_function(board)

    min_move = None
    min_val = 9999

    for move in board.legal_moves:
        if min_move is None:
            min_move = move
        if move not in moves:
            board.push(move)
            curr_val = max(board, depth - 1, alpha, beta, moves)
            if curr_val > beta:
                board.pop()
                return curr_val
            if curr_val is not None and (min_val is None or curr_val < min_val):
                min_val = curr_val
                min_move = move
                alpha = curr_val

            board.pop()

    return min_val


def max(board, depth, alpha, beta, moves):

    if(depth == 0):
        return eval_function(board)

    max_move = None
    max_val = -9999

    for move in board.legal_moves:
        if max_move is None:
            max_move = move
        if move not in moves:
            board.push(move)
            curr_val = min(board, depth - 1, alpha, beta, moves)
            if(curr_val < alpha):
                board.pop()
                return curr_val
            if curr_val is not None and (max_val is None or curr_val > max_val):
                max_val = curr_val
                max_move = move
                beta = curr_val
            board.pop()

    return max_val


def alphabeta(board, depth, moves):

    if board.turn == chess.BLACK:
        print("board turn is white")
        if(depth == 0):
            return eval_function(board)

        min_move = None
        min_val = 9999

        # alpha is the upper bound, beta is the lower bound

        alpha = -9999
        beta = 9999

        for move in board.legal_moves:
            if min_move is None:
                min_move = move
            if move not in moves:
                board.push(move)
                curr_val = max(board, depth - 1, alpha, beta, moves)
                if curr_val is not None and (min_val is None or curr_val < min_val):
                    min_val = curr_val
                    min_move = move
                    alpha = curr_val
                board.pop()

        return min_move

    elif board.turn == chess.WHITE:
        print("board turn is black")

        if(depth == 0):
            return eval_function(board)

        max_move = None
        max_val = -9999

        # alpha is the upper bound, beta is the lower bound

        alpha = -9999
        beta = 9999

        for move in board.legal_moves:
            if max_move is None:
                max_move = move
            if move not in moves:
                board.push(move)
                curr_val = min(board, depth - 1, alpha, beta, moves)
                if curr_val is not None and (max_val is None or curr_val > max_val):
                    max_val = curr_val
                    max_move = move
                    beta = curr_val
                board.pop()

        return max_move


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
