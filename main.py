from chessengine import ChessEngine
from time import sleep
import berserk
from local import API_TOKEN
import chess
from pprint import pprint
from engine import ChessEngine

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


class Game:
    def __init__(self, client, game_id, **kwargs):
        super().__init__(**kwargs)
        self.game_id = game_id
        self.client = client
        self.stream = client.bots.stream_game_state(game_id)
        self.current_state = next(self.stream)
        self.side = None
        self.synchronized = False

        try:
            if self.current_state['white']['id'] == 'yatsenkoa-bot':
                # the side is white
                self.side = chess.WHITE

        except Exception as e:
            # the side is probably not white
            if self.current_state['black']['id'] == 'yatsenkoa-bot':
                self.side = chess.BLACK

        self.engine = ChessEngine(self.side)

        # the opponent is waiting for our first move
        if self.side == chess.WHITE and self.current_state['state']['moves'] == '':
            self.make_move()
            # dont need to sync
            self.synchronized = True

    def run(self):
        for event in self.stream:
            if event['type'] == 'gameState':
                self.handle_state_change(event)
            elif event['type'] == 'chatLine':
                self.handle_chat_line(event)

    def make_move(self):
        ai_move = self.engine.ai_move()
        if ai_move == None:
            print("Surrendering...")
            self.client.bots.abort_game(self.game_id)
        self.client.bots.make_move(self.game_id, ai_move)

    def handle_state_change(self, game_state):
        game_state_moves = game_state['moves'].split(' ')

        if self.side == chess.BLACK and len(game_state_moves) % 2 == 1:
            if not self.synchronized:
                self.engine.synchronize(game_state_moves)
                self.synchronized = True
            else:
                self.engine.push_move(game_state_moves[-1])
            self.make_move()

        elif self.side == chess.WHITE and len(game_state_moves) % 2 == 0:
            if not self.synchronized:
                self.engine.synchronize(game_state_moves)
                self.synchronized = True
            else:
                self.engine.push_move(game_state_moves[-1])
            self.make_move()

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
