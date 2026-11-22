# evaluate.py
# Plays many games of AI vs. random and AI vs. greedy and prints the metrics.
# Run:  python evaluate.py
from board import Board, TERRAIN_MAPS
from minimax import ai_move
from opponents import random_move, greedy_move

GAMES = 100     # games per opponent
DEPTH = 4       # how many moves ahead the AI looks


def play_game(opponent, values, ai_starts):
    # Play one full game. Returns AI score minus opponent score.
    board = Board(values)
    board.turn = "A" if ai_starts else "P"
    while not board.is_over():
        if board.turn == "A":
            move = ai_move(board, DEPTH)
        else:
            move = opponent(board)
        board.make_move(move)
    return board.scores["A"] - board.scores["P"]


def run(opponent, name):
    maps = list(TERRAIN_MAPS.values())
    wins = losses = ties = 0
    total_diff = 0
    for i in range(GAMES):
        values = maps[(i // 2) % len(maps)]        # rotate through the maps
        diff = play_game(opponent, values, ai_starts=(i % 2 == 0))  # alternate who starts
        total_diff += diff
        if diff > 0:
            wins += 1
        elif diff < 0:
            losses += 1
        else:
            ties += 1
    print(f"AI vs {name}: {wins} wins, {losses} losses, {ties} ties  "
          f"| win rate {wins / GAMES:.0%}  | avg score difference {total_diff / GAMES:+.2f}")


if __name__ == "__main__":
    run(random_move, "random")
    run(greedy_move, "greedy")