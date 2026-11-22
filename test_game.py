# test_game.py
# Correctness checks for the game rules and the minimax AI.
# Run:  python test_game.py
# Each test sets up a small situation where we KNOW the right answer,
# then uses `assert` to check the code gets it. If an assert is wrong, Python stops with an error.
from board import Board, TERRAIN_MAPS
from minimax import ai_move


def test_completing_box_scores_and_gives_extra_turn():
    board = Board(TERRAIN_MAPS["valley"])
    # Draw 3 sides of the top-left box (worth 3) directly.
    board.h[0][0] = "P"     # top
    board.h[1][0] = "P"     # bottom
    board.v[0][0] = "P"     # left
    board.turn = "P"
    board.make_move(("v", 0, 1))            # right side finishes the box
    assert board.owner[0][0] == "P"         # player owns it
    assert board.scores["P"] == 3           # got its terrain value
    assert board.turn == "P"                # finishing a box = go again
    print("PASS: completing a box scores its value and gives an extra turn")


def test_turn_switches_when_no_box_completed():
    board = Board(TERRAIN_MAPS["valley"])
    board.turn = "P"
    board.make_move(("h", 0, 0))            # first line can't finish anything
    assert board.turn == "A"                # so it's the AI's turn now
    assert board.scores == {"A": 0, "P": 0}
    print("PASS: turn switches when no box is completed")


def test_negative_box_subtracts_points():
    board = Board(TERRAIN_MAPS["valley"])
    # Top-middle box is worth -2. Draw 3 sides.
    board.h[0][1] = "P"
    board.h[1][1] = "P"
    board.v[0][1] = "P"
    board.turn = "P"
    board.make_move(("v", 0, 2))
    assert board.scores["P"] == -2
    print("PASS: capturing negative terrain lowers your score")


def test_ai_takes_valuable_box():
    board = Board(TERRAIN_MAPS["valley"])
    # Center box is worth 8. Leave only its right side open.
    board.h[1][1] = "P"
    board.h[2][1] = "P"
    board.v[1][1] = "P"
    board.turn = "A"
    move = ai_move(board)
    assert move == ("v", 1, 2), f"AI chose {move}"   # the line that finishes the 8 box
    print("PASS: AI completes a high-value box when it can")


def test_ai_avoids_negative_box():
    board = Board(TERRAIN_MAPS["valley"])
    # Top-middle box is worth -2. Leave only its right side open.
    board.h[0][1] = "P"
    board.h[1][1] = "P"
    board.v[0][1] = "P"
    board.turn = "A"
    move = ai_move(board)
    assert move != ("v", 0, 2), "AI took the -2 box"  # taking it would lower the AI's score
    print("PASS: AI avoids completing a negative box when it has other options")


if __name__ == "__main__":
    test_completing_box_scores_and_gives_extra_turn()
    test_turn_switches_when_no_box_completed()
    test_negative_box_subtracts_points()
    test_ai_takes_valuable_box()
    test_ai_avoids_negative_box()
    print("\nAll tests passed.")