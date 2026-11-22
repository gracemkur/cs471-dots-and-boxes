# play.py
# Play against the AI in the terminal.  Run:  python play.py
from board import Board, TERRAIN_MAPS
from minimax import ai_move


def ask_move(board):
    # Keep asking until the player types a legal move.
    while True:
        parts = input("Your move (e.g. h 0 1): ").split()
        if len(parts) == 3 and parts[0] in ("h", "v") and parts[1].isdigit() and parts[2].isdigit():
            move = (parts[0], int(parts[1]), int(parts[2]))
            if move in board.available_moves():
                return move
        print("Invalid move. Type h or v, then row, then column, for a line not drawn yet.")


def main():
    print("Terrain Dots and Boxes")
    print("  h r c = horizontal line from dot (r, c) to dot (r, c+1)")
    print("  v r c = vertical line from dot (r, c) to dot (r+1, c)")
    print("Finish a box to claim its terrain value (negatives hurt!) and go again.\n")

    name = input(f"Choose a map {list(TERRAIN_MAPS)}: ").strip()
    if name not in TERRAIN_MAPS:
        name = "valley"
    board = Board(TERRAIN_MAPS[name])

    while not board.is_over():
        board.display()
        if board.turn == "P":
            move = ask_move(board)
        else:
            move = ai_move(board)
            print(f"AI draws: {move[0]} {move[1]} {move[2]}")
        board.make_move(move)

    board.display()
    if board.scores["A"] > board.scores["P"]:
        print("AI wins.")
    elif board.scores["P"] > board.scores["A"]:
        print("You win!")
    else:
        print("Tie.")


if __name__ == "__main__":
    main()