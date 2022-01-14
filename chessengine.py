import chess
from chess import Board
from alphabeta import alphabeta
# AI: given a board and a player (black or white), return the best Chess.Move

DEPTH = 3

class ChessEngine():

    moves = dict()
    moves[chess.WHITE] = []
    moves[chess.BLACK] = []

    def __init__(self, ai=alphabeta):
        self.ai = ai
        self.board = Board()
    
    def ai_move(self):
        nextmove = self.ai(self.board, DEPTH, self.moves[self.board.turn])
        while nextmove in self.moves[self.board.turn]:
            nextmove = self.ai(self.board, DEPTH, self.moves[self.board.turn])
        self.moves[self.board.turn].append(nextmove)
        self.board.push(nextmove)
        return str(nextmove)

    def output(self, s):
        print(s)
    
    def reset_game(self):
        self.moves[chess.WHITE] = []
        self.moves[chess.BLACK] = []
        self.board = Board()

    def push_move_white(self, move_str):
        move = chess.Move.from_uci(move_str)
        self.moves[chess.WHITE].push(move)
        self.board.push(move)

    def push_move_black(self, move_str):
        move = chess.Move.from_uci(move_str)
        self.moves[chess.BLACK].push(move)
        self.board.push(move)


    def uci_mode(self):
        # uci mode for chess bot executable
    
        our_time, opp_time = 1000, 1000 # time in centi-seconds
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
