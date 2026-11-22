CS471 Final Project: Terrain Dots and Boxes

Dots and Boxes on a 4x4 dot grid (3x3 boxes). Each box has a terrain value, and some values are negative, so capturing every box you can is not always the best strategy. The AI uses minimax with alpha-beta pruning (CS471 adversarial search).

Team: [Name 1], [Name 2], [Name 3]

Setup
Dependencies: Python 3.8 or newer. No other packages are needed (standard library only).
Get the code:
git clone https://github.com/gracemkur/cs471-dots-and-boxes.git
cd cs471-dots-and-boxes
How to run
python play.py        # play against the AI in the terminal
python test_game.py   # correctness tests (5 checks)
python evaluate.py    # AI vs random and greedy opponents, 100 games each (~10 sec)

On some systems, use python3 instead of python.

How to play

Dots are numbered by row (down) and column (across), starting at 0.

h r c: horizontal line from dot (r, c) to dot (r, c+1)
v r c: vertical line from dot (r, c) to dot (r+1, c)

Finishing the 4th side of a box claims it, adds its terrain value (which can be negative) to your score, and gives you another turn. Your lines show as ----- and |, and the AI's lines show as ===== and #.

Files
File	What it does
board.py	Terrain maps, lines, boxes, scoring, extra-turn rule, ASCII display
minimax.py	Minimax + alpha-beta; evaluation = AI score - opponent score
opponents.py	Random and greedy baseline opponents
play.py	Terminal game: human (P) vs AI (A)
test_game.py	Correctness tests for game rules and AI decisions
evaluate.py	Win rate and average score difference over many games
PROGRESS.md	Checkpoint progress summary
Correctness tests

test_game.py checks:

Completing a box adds its value and gives an extra turn.
The turn switches when no box is completed.
Capturing a negative box lowers the score.
The AI completes a high-value (8) box when one is available.
The AI avoids completing a negative (-2) box when it has other moves.
AI use

AI coding assistants (Claude) were used to help write this code, as permitted by the course. Every team member has reviewed it and can explain it.