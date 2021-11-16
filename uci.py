from __future__ import print_function
from __future__ import division
import importlib
import re
import sys
import time
import logging
import argparse

import tools
import sunfish

from chess_runner import ChessRunner
import chess
from alphabeta import alphabeta

class ChessRunner():
    def __init__():
        self.board = chess.Board()  
    
    def handle_move(uci_move : str):  
        move = chess.Move.from_uci(uci_move)
        board.push(move)
    
    def get_ai_move():
        ai_move = alphabeta(board, 7) 
        board.push(ai_move)
        return str(ai_move)

def main():

    def output(line):
        print(line, file=out)
        logging.debug(line)

    our_time, opp_time = 1000, 1000 # time in centi-seconds

    stack = []
    
    runner = None

    while True:
        if stack:
            smove = stack.pop()
        else:
            smove = input()

        logging.debug(f'>>> {smove} ')

        if smove == 'quit':
            break

        elif smove == 'uci':
            output('id name ai-chess')
            output('id author Artem Yatsenko')
            output('uciok')

        elif smove == 'isready':
            output('readyok')

        elif smove == 'ucinewgame':
            runner = ChessRunner()

        # syntax specified in UCI
        # position [fen  | startpos ]  moves  ....

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

            elif params[1] == 'startpos':
                fen = tools.FEN_INITIAL

            else:
                pass

            pos = tools.parseFEN(fen)
            color = WHITE if fen.split()[1] == 'w' else BLACK

            for move in moveslist:
                pos = pos.move(tools.mparse(color, move))
                color = 1 - color

        elif smove.startswith('go'):
            #  default options
            depth = 1000
            movetime = -1

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
            # We only resign once we are mated.. That's never?
            if s == -sunfish.MATE_UPPER:
                output('resign')
            else:
                moves = moves.split(' ')
                if len(moves) > 1:
                    output(f'bestmove {moves[0]} ponder {moves[1]}')
                else:
                    output('bestmove ' + moves[0])

        elif smove.startswith('time'):
            our_time = int(smove.split()[1])

        elif smove.startswith('otim'):
            opp_time = int(smove.split()[1])

        else:
            pass

if __name__ == '__main__':
    main()
