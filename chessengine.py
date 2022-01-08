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
        return nextmove.to_uci()
    
    def uci_mode(self):
        # uci mode for chess bot executable
    
        our_time, opp_time = 1000, 1000 # time in centi-seconds
        stack = []

        while True:

            smove = input()

            if smove == 'quit':
                break
            
            elif smove == 'uci':
                output('id name ai-chess')
                output('id author Artem Yatsenko')
                output('uciok')

            elif smove == 'isready':
                output('readyok')
            
            elif smove == 'register':
                output('later')
            
            elif smove == 'ucinewgame':
                runner = ChessRunner()

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
                    self.board.set_board_fen(fen)
                    for move_uci in moveslist:
                        self.board.push(chess.Move.from_uci(move_uci))
                 
            elif smove == 'go':

                fen_move = self.ai_move()

                print(f'bestmove ' + fen_move)

            else:
                pass