import chess

SEARCH_DEPTH = 2

def eval_function(board):

    # if the state is a winning state, add 1000 points
    # minimax: white is the positive player, black is the negative  

    NUM_KINGS_WHITE = len(board.pieces(piece_type=chess.KING, color=chess.WHITE))
    NUM_KINGS_BLACK = len(board.pieces(piece_type=chess.KING, color=chess.BLACK))
     
    NUM_QUEENS_WHITE = len(board.pieces(piece_type=chess.QUEEN, color=chess.WHITE))
    NUM_QUEENS_BLACK = len(board.pieces(piece_type=chess.QUEEN, color=chess.BLACK))
    
    NUM_ROOKS_WHITE = len(board.pieces(piece_type=chess.ROOK, color=chess.WHITE))
    NUM_ROOKS_BLACK = len(board.pieces(piece_type=chess.ROOK, color=chess.BLACK))

    NUM_BISHOPS_WHITE = len(board.pieces(piece_type=chess.BISHOP, color=chess.WHITE))
    NUM_BISHOPS_BLACK = len(board.pieces(piece_type=chess.BISHOP, color=chess.BLACK))

    NUM_KNIGHTS_WHITE = len(board.pieces(piece_type=chess.KNIGHT, color=chess.WHITE))
    NUM_KNIGHTS_BLACK = len(board.pieces(piece_type=chess.KNIGHT, color=chess.BLACK))
    
    NUM_PAWNS_WHITE = len(board.pieces(piece_type=chess.PAWN, color=chess.WHITE))
    NUM_PAWNS_BLACK = len(board.pieces(piece_type=chess.PAWN, color=chess.BLACK))

    f = 0
    f += 200 * (NUM_KINGS_WHITE - NUM_KINGS_BLACK)
    f += 9 * (NUM_QUEENS_WHITE - NUM_QUEENS_BLACK)
    f += 5 * (NUM_ROOKS_WHITE - NUM_ROOKS_BLACK)
    f += 3 * (NUM_BISHOPS_WHITE - NUM_BISHOPS_BLACK)
    f += 3 * (NUM_KNITGHTS_WHITE - NUM_KNIGHTS_BLACK)
    f += 1 * (NUM_PAWNS_WHITE - NUM_PAWNS_BLACK) 


def minimax(board, depth):
    

def compute_move(board): 

    for move in board.legal_moves:
if __name__ == "__main__":
    
    print("Starting pos:")
    board = chess.Board()
    print(board)
    print()

    while not board.is_variant_win() and not board.is_variant_loss():
        
        print("Current turn: " )
        print("WHITE" if board.turn else "BLACK")
        print()
        print(board)
        print('a|b|c|d|e|f|g|h')
        print()

        if board.turn:
            user_move = input()
            move = chess.Move.from_uci(user_move) 

            while move not in board.legal_moves:
                print("Invalid move, try again...")
                
                user_move = input()
                move = chess.Move.from_uci(user_move)
                
            board.push(move)
        else:
            ai_move = compute_move(board)
            board.push(ai_move)

        
    turn = "WHITE" if board.turn else "BLACK"
    print(turn + " won")
            
        
            
            
        
	   


