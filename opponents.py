# opponents.py
# Simple baseline opponents to test the AI against.
import random


def random_move(board):
    # Pick any legal line at random.
    return random.choice(board.available_moves())


def greedy_move(board):
    # Pick the move that gives the most points RIGHT NOW (no looking ahead).
    me = board.turn
    best_gain = None
    best_moves = []
    for move in board.available_moves():
        child = board.copy()
        child.make_move(move)
        gain = child.scores[me] - board.scores[me]   # points earned by this one move
        if best_gain is None or gain > best_gain:
            best_gain = gain
            best_moves = [move]
        elif gain == best_gain:
            best_moves.append(move)
    # Break ties randomly so the greedy player isn't predictable.
    return random.choice(best_moves)