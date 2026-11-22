# board.py
# The game itself: the grid, the lines, the boxes, the scores, and whose turn it is.

# Terrain maps. Each number is how many points a box is worth.
# Negative boxes are bad terrain - capturing them LOSES points.
# A 4x4 grid of dots makes a 3x3 grid of boxes.
TERRAIN_MAPS = {
    "valley": [
        [3, -2, 5],
        [1, 8, -4],
        [-1, 2, 4],
    ],
    "ridge": [
        [-3, 6, -1],
        [4, -5, 7],
        [2, 1, -2],
    ],
}


class Board:
    def __init__(self, values):
        self.values = values              # point value of each box
        self.rows = len(values)           # number of box rows (3)
        self.cols = len(values[0])        # number of box columns (3)

        # Horizontal lines: h[r][c] is the line from dot (r, c) to dot (r, c+1).
        # There are rows+1 rows of dots, and cols lines across each one.
        self.h = [[False] * self.cols for _ in range(self.rows + 1)]

        # Vertical lines: v[r][c] is the line from dot (r, c) to dot (r+1, c).
        # There are rows lines down, and cols+1 columns of dots.
        self.v = [[False] * (self.cols + 1) for _ in range(self.rows)]

        # Who owns each box: None (nobody yet), "A" (AI), or "P" (player/opponent).
        self.owner = [[None] * self.cols for _ in range(self.rows)]

        self.scores = {"A": 0, "P": 0}    # running terrain score for each side
        self.turn = "P"                   # player goes first by default

    def copy(self):
        # Minimax tries moves on copies so it never changes the real board.
        new = Board(self.values)
        new.h = [row[:] for row in self.h]          # row[:] copies a list
        new.v = [row[:] for row in self.v]
        new.owner = [row[:] for row in self.owner]
        new.scores = dict(self.scores)
        new.turn = self.turn
        return new

    def available_moves(self):
        # A move is a tuple: ("h", r, c) or ("v", r, c) for any line not drawn yet.
        moves = []
        for r in range(self.rows + 1):
            for c in range(self.cols):
                if not self.h[r][c]:
                    moves.append(("h", r, c))
        for r in range(self.rows):
            for c in range(self.cols + 1):
                if not self.v[r][c]:
                    moves.append(("v", r, c))
        return moves

    def box_done(self, r, c):
        # A box is complete when its top, bottom, left, and right lines are all drawn.
        return self.h[r][c] and self.h[r + 1][c] and self.v[r][c] and self.v[r][c + 1]

    def make_move(self, move):
        kind, r, c = move

        # Draw the line and figure out which two boxes it could finish.
        # Store WHO drew the line ("A" or "P") instead of just True.
        # Python treats "A" and "P" as true, so the rest of the code still works.
        if kind == "h":
            self.h[r][c] = self.turn
            touching = [(r - 1, c), (r, c)]   # box above the line, box below it
        else:
            self.v[r][c] = self.turn
            touching = [(r, c - 1), (r, c)]   # box left of the line, box right of it

        completed = 0
        for br, bc in touching:
            # Skip "boxes" that are off the edge of the board.
            if 0 <= br < self.rows and 0 <= bc < self.cols:
                if self.box_done(br, bc):
                    self.owner[br][bc] = self.turn                 # claim it
                    self.scores[self.turn] += self.values[br][bc]  # add its terrain value
                    completed += 1

        # Dots and Boxes rule: finishing a box gives you another turn.
        # Otherwise, the turn passes to the other side.
        if completed == 0:
            self.turn = "A" if self.turn == "P" else "P"

    def is_over(self):
        # The game ends when every line has been drawn.
        return len(self.available_moves()) == 0

    def display(self):
        # Column numbers across the top (one per dot column).
        print("    " + "".join(f"{c:<6}" for c in range(self.cols + 1)))

        for r in range(self.rows + 1):
            # Row of dots, with horizontal lines between them if drawn.
            line = f"{r:<4}"
            for c in range(self.cols):
                if self.h[r][c] == "A":
                    line += "*====="      # AI's line
                elif self.h[r][c] == "P":
                    line += "*-----"      # your line
                else:
                    line += "*     "      # not drawn yet
            line += "*"
            print(line)

            # Below the last row of dots there are no more boxes.
            if r == self.rows:
                break

            # Row of boxes: vertical lines, plus the box's value or its owner.
            line = "    "
            for c in range(self.cols + 1):
                if self.v[r][c] == "A":
                    line += "#"           # AI's line
                elif self.v[r][c] == "P":
                    line += "|"           # your line
                else:
                    line += " "           # not drawn yet
                if c < self.cols:
                    text = self.owner[r][c] or str(self.values[r][c])
                    line += f"{text:^5}"     # center text in 5 spaces
            print(line)

        print("Your lines: ----- |     AI lines: ===== #")
        print(f"Score -> You (P): {self.scores['P']}   AI (A): {self.scores['A']}")
        print()