from chessengine import ChessEngine
from time import sleep

def selfplay():
    engine = ChessEngine()
    i = 0

    while not engine.board.is_game_over():
        i += 1
        print(engine.board)
        print()
        engine.ai_move()
    print("game is over")
    print(engine.board.outcome())
    print(i)

def ucimode():
    engine = ChessEngine()
    engine.uci_mode()

if __name__ == "__main__":
    ucimode()
