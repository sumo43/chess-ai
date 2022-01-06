from chessengine import ChessEngine


engine = ChessEngine()
print(engine.board)
engine.ai_move()
print(engine.board)


def selfplay():
    engine = ChessEngine()

    while not engine.is_game_over():
        print(engine)
        engine.ai_move()