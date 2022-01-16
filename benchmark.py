import chess
from chessengine import ChessEngine
import cProfile


# indended to be run with cprofile


def benchmark():
    engine = ChessEngine(True)
    move = engine.ai_move()
    engine.print_board()


if __name__ == "__main__":
    benchmark()
