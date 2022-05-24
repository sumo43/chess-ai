import chess
from chess import Board
from alphabeta import alphabeta
from minimax import compute_min

"""

Chess Runner interacts with UCI. 
designed to be sued with different chess engines

"""

MAX_DEPTH = 3


class ChessRunner():

    moves = dict()
    maximizing_player = None

    def __init__(self, maximizing_player, ai=alphabeta):
        self.ai = ai
        self.board = Board()
        self.maximizing_player = maximizing_player

    def ai_move(self):
        nextmove = self.ai(self.board, self.maximizing_player, MAX_DEPTH)
        """
        while nextmove in self.moves[self.board.turn]:
            nextmove = self.ai(self.board, self.maximizing_player, 3)
        """
        print(self.board)
        if nextmove == None:
            return None
        self.board.push(nextmove)
        return str(nextmove)

    def output(self, s):
        print(s)

    def print_board(self):
        print(self.board)

    def reset_game(self):
        self.board = Board()

    def push_move_exp(self, move_str, move_side):
        move = chess.Move.from_uci(move_str)
        if move_side == True:
            self.moves[chess.WHITE].append(move)
        else:
            self.moves[chess.BLACK].append(move)
        self.board.push(move)

    def push_move(self, move_str):
        self.board.push(chess.Move.from_uci(move_str))

    def synchronize(self, list_moves):
        for move in list_moves:
            self.push_move(move)
        print("synced")
        print(self.board)

    def uci_mode(self):
        # uci mode for chess bot executable

        our_time, opp_time = 1000, 1000  # time in centi-seconds
        stack = []

        while True:

            smove = input()

            if smove == 'quit':
                break

            elif smove == 'uci':
                self.output('id name ai-chess')
                self.output('id author Artem Yatsenko')
                self.output('uciok')

            elif smove == 'isready':
                self.output('readyok')

            elif smove == 'register':
                self.output('later')

            elif smove == 'ucinewgame':
                self.reset_game()
                pass

            elif smove.startswith('position'):
                params = smove.split(' ')
                idx = smove.find('moves')

                if idx >= 0:
                    moveslist = smove[idx:].split()[1:]
                else:
                    moveslist = []

                if params[1] == 'startpos':
                    # use the starting board state
                    for move_uci in moveslist:
                        self.board.push(chess.Move.from_uci(move_uci))
                else:
                    fen = params[1]
                    if self.board.fen() != fen:
                        self.board.set_board_fen(fen)
                    for move_uci in moveslist:
                        self.board.push(chess.Move.from_uci(move_uci))

            elif smove.startswith('go'):

                fen_move = self.ai_move()

                self.output('bestmove ' + fen_move)

            else:
                pass
