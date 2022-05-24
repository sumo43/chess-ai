import chess


def naive_eval_function(board):

    # if the state is a winning state, add 1000 points
    # minimax: white is the positive player, black is the negative

    NUM_KINGS_WHITE = len(board.pieces(
        piece_type=chess.KING, color=chess.WHITE))
    NUM_KINGS_BLACK = len(board.pieces(
        piece_type=chess.KING, color=chess.BLACK))

    NUM_QUEENS_WHITE = len(board.pieces(
        piece_type=chess.QUEEN, color=chess.WHITE))
    NUM_QUEENS_BLACK = len(board.pieces(
        piece_type=chess.QUEEN, color=chess.BLACK))

    NUM_ROOKS_WHITE = len(board.pieces(
        piece_type=chess.ROOK, color=chess.WHITE))
    NUM_ROOKS_BLACK = len(board.pieces(
        piece_type=chess.ROOK, color=chess.BLACK))

    NUM_BISHOPS_WHITE = len(board.pieces(
        piece_type=chess.BISHOP, color=chess.WHITE))
    NUM_BISHOPS_BLACK = len(board.pieces(
        piece_type=chess.BISHOP, color=chess.BLACK))

    NUM_KNIGHTS_WHITE = len(board.pieces(
        piece_type=chess.KNIGHT, color=chess.WHITE))
    NUM_KNIGHTS_BLACK = len(board.pieces(
        piece_type=chess.KNIGHT, color=chess.BLACK))

    NUM_PAWNS_WHITE = len(board.pieces(
        piece_type=chess.PAWN, color=chess.WHITE))
    NUM_PAWNS_BLACK = len(board.pieces(
        piece_type=chess.PAWN, color=chess.BLACK))

    f = 0
    f += 200 * (NUM_KINGS_WHITE - NUM_KINGS_BLACK)
    f += 9 * (NUM_QUEENS_WHITE - NUM_QUEENS_BLACK)
    f += 5 * (NUM_ROOKS_WHITE - NUM_ROOKS_BLACK)
    f += 3 * (NUM_BISHOPS_WHITE - NUM_BISHOPS_BLACK)
    f += 3 * (NUM_KNIGHTS_WHITE - NUM_KNIGHTS_BLACK)
    f += 1 * (NUM_PAWNS_WHITE - NUM_PAWNS_BLACK)

    return f
