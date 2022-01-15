from chessengine import ChessEngine
from time import sleep
import berserk
from local import API_TOKEN
import threading
import chess
from pprint import pprint


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
        self.engine = ChessEngine()

        self.side = None

        try:
            if self.current_state['white']['id'] == 'yatsenkoa-bot':
                # the side is white
                self.side = chess.WHITE

        except Exception as e:
            # the side is probably not white
            if self.current_state['black']['id'] == 'yatsenkoa-bot':
                self.side = chess.BLACK

        # the opponent is waiting for our first move
        if self.side == chess.WHITE and self.current_state['state']['moves'] == '':
            self.first_move()

    def run(self):
        for event in self.stream:
            if event['type'] == 'gameState':
                self.handle_state_change(event)
            elif event['type'] == 'chatLine':
                self.handle_chat_line(event)

    def first_move(self):
        sides = []
        ai_move = self.engine.ai_move()
        self.client.bots.make_move(self.game_id, ai_move)

    def handle_state_change(self, game_state):

        self.engine.reset_game()

        game_state_moves = game_state['moves'].split(' ')
        i = 0
        # white, black, white, black...
        sides = [chess.WHITE, chess.BLACK]

        for move in game_state_moves:
            self.engine.push_move(move)

        if self.side == chess.BLACK and len(game_state_moves) % 2 == 1:
            ai_move = self.engine.ai_move()
            self.client.bots.make_move(self.game_id, ai_move)

        elif self.side == chess.WHITE and len(game_state_moves) % 2 == 0:
            ai_move = self.engine.ai_move()
            self.client.bots.make_move(self.game_id, ai_move)

    def handle_chat_line(self, chat_line):
        print(chat_line)
        pass


if __name__ == "__main__":
    session = berserk.TokenSession(API_TOKEN)
    client = berserk.Client(session=session)

    for event in client.bots.stream_incoming_events():
        game_id = event['game']['id']
        if event['type'] == 'challenge':
            cliennt.bots.accept_challenge(game_id)
        elif event['type'] == 'gameStart':
            game = Game(client, game_id)
            game.start()
