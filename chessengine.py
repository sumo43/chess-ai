from chess import Board
from alphabeta import alphabeta
# AI: given a board and a player (black or white), return the best Chess.Move

class ChessEngine():
    def __init__(self, ai=alphabeta):
        self.ai = ai
        self.board = Board()
    
    def ai_move(self):
        nextmove = self.ai(self.board)
        self.board.push(nextmove)
    