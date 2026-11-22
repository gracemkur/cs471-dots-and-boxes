# CS471 Final Project: Terrain Dots and Boxes

Dots and Boxes on a 4x4 dot grid (3x3 boxes). Each box has a terrain value, and some values are negative, so capturing every box you can is not always the best strategy. The AI uses **minimax with alpha-beta pruning** (CS471 adversarial search).

## How to run
No packages are needed, only Python 3.

```
python play.py       # play against the AI in the terminal
python evaluate.py   # AI vs random and greedy opponents, 100 games each
```

## Files
| File | What it does |
|---|---|
| `board.py` | Terrain maps, lines, boxes, scoring, extra-turn rule, ASCII display |
| `minimax.py` | Minimax + alpha-beta; evaluation = AI score - opponent score |
| `opponents.py` | Random and greedy baseline opponents |
| `play.py` | Terminal game: human (P) vs AI (A) |
| `evaluate.py` | Win rate and average score difference over many games |

## Moves
- `h r c`: horizontal line from dot (r, c) to dot (r, c+1)
- `v r c`: vertical line from dot (r, c) to dot (r+1, c)

## AI use
AI tools (Claude) were used to help write this code. Every team member reviewed it and can explain it.