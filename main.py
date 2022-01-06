from chessengine import ChessEngine
from time import sleep



def selfplay():
    engine = ChessEngine()

    while not engine.board.is_game_over():
        print(engine.board)
        print()
        engine.ai_move()
        sleep(1)

if __name__ == "__main__":
    """
    engine = ChessEngine()
    engine.ai_move()
    """
    selfplay()