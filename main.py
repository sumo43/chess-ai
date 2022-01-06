from chessengine import ChessEngine

def selfplay():
    engine = ChessEngine()

    while not engine.is_game_over():
        print(engine)
        engine.move()