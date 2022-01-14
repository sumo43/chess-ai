from chessengine import ChessEngine
from time import sleep
import berserk
from local import API_TOKEN
import threading

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

class Game(threading.Thread):
    def __init__(self, client, game_id, **kwargs):
        super().__init__(**kwargs)
        self.game_id = game_id
        self.client = client
        self.stream = client.bots.stream_game_state(game_id)
        self.current_state = next(self.stream)

    def run(self):
        for event in self.stream:
            if event['type'] == 'gameState':
                self.handle_state_change(event)
            elif event['type'] == 'chatLine':
                self.handle_chat_line(event)

    def handle_state_change(self, game_state):
        pass

    def handle_chat_line(self, chat_line):
        pass

if __name__ == "__main__":

    session = berserk.TokenSession(API_TOKEN)
    client = berserk.Client(session=session)
