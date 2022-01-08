import chess
from chess import Board
from alphabeta import alphabeta
# AI: given a board and a player (black or white), return the best Chess.Move

class ChessEngine():

    moves = dict()
    moves[chess.WHITE] = []
    moves[chess.BLACK] = []

    def __init__(self, ai=alphabeta):
        self.ai = ai
        self.board = Board()
    
    def ai_move(self):
        nextmove = self.ai(self.board, 3, self.moves[self.board.turn])
        while nextmove in self.moves[self.board.turn]:
            nextmove = self.ai(self.board, 3, self.moves[self.board.turn])
        self.moves[self.board.turn].append(nextmove)
        self.board.push(nextmove)
    
    def uci_mode(self):
        # uci mode for chess bot executable
    
        our_time, opp_time = 1000, 1000 # time in centi-seconds

        while True:

            if stack:
                smove = stack.pop()
            else:
                smove = input()

            logging.debug(f'>>> {smove} ')

            if smove == 'quit':
                break
            
            # answer query for uci info
            elif smove == 'uci':
                output('id name ai-chess')
                output('id author Artem Yatsenko')
                output('uciok')

            elif smove == 'isready':
                output('readyok')
            
            elif smove == 'register':
                output('later')
            
            # we dont need to do anything else here, since chessrunner already starts with an initial state
            elif smove == 'ucinewgame':
                runner = ChessRunner()

            # syntax specified in UCI
            # position [fen  | startpos ]  moves  ....

            # if it starts with position, try to find moves. The moves will be after that string
            # unless the position is startpos, in which case just use the starting position of the board
            # if there is a single move, it also may be in this format: position fen a3a5

            elif smove.startswith('position'):
                params = smove.split(' ')
                idx = smove.find('moves')

                if idx >= 0:
                    moveslist = smove[idx:].split()[1:]
                else:
                    moveslist = []
                if params[1] == 'fen':
                    if idx >= 0:
                        fenpart = smove[:idx]
                    else:
                        fenpart = smove

                    _, _, fen = fenpart.split(' ', 2)

                    runner.player_move_from_uci(moveslist[0], fen)

                elif params[1] == 'startpos':
                    # use the starting board state
                    runner.player_move_from_uci(moveslist[0], chess.STARTING_FEN) 
                    pass
            
            elif smove.startswith('go'):
                #  default options
                """
                _, *params = smove.split(' ')
                for param, val in zip(*2*(iter(params),)):
                    if param == 'depth':
                        depth = int(val)
                    if param == 'movetime':
                        movetime = int(val)
                    if param == 'wtime':
                        our_time = int(val)
                    if param == 'btime':
                        opp_time = int(val)

                moves_remain = 40

                start = time.time()
                ponder = None
                for sdepth, _move, _score in searcher.search(pos):
                    moves = tools.pv(searcher, pos, include_scores=False)

                    if show_thinking:
                        entry = searcher.tp_score.get((pos, sdepth, True))
                        score = int(round((entry.lower + entry.upper)/2))
                        usedtime = int((time.time() - start) * 1000)
                        moves_str = moves if len(moves) < 15 else ''
                        output('info depth {} score cp {} time {} nodes {} pv {}'.format(sdepth, score, usedtime, searcher.nodes, moves_str))

                    if len(moves) > 5:
                        ponder = moves[1]

                    if movetime > 0 and (time.time() - start) * 1000 > movetime:
                        break

                    if (time.time() - start) * 1000 > our_time/moves_remain:
                        break

                    if sdepth >= depth:
                        break

                entry = searcher.tp_score.get((pos, sdepth, True))
                m, s = searcher.tp_move.get(pos), entry.lower
                """
                ai_move = runner.get_ai_move()
                output('bestmove ' + ai_move)

            elif smove.startswith('time'):
                our_time = int(smove.split()[1])

            elif smove.startswith('otim'):
                opp_time = int(smove.split()[1])

            else:
                pass