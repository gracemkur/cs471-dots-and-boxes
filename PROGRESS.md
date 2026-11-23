Checkpoint Progress Summary
Completed functionality

We built a terminal version of Dots and Boxes on a 4x4 dot grid, where each of the 9 boxes has a terrain value from -5 to +8. The game handles drawing lines, detecting completed boxes, adding terrain value to the capturing side's score, and the extra-turn rule. Two terrain maps ("valley" and "ridge") are included. A human can play against the AI using typed moves (h r c / v r c), and the board and scores are printed after every move.

The AI uses minimax with alpha-beta pruning, searching 4 moves ahead. It scores positions as AI score minus opponent score, and it accounts for extra turns by checking whose turn it is at each step of the search. We wrote five correctness tests (test_game.py) covering scoring, turn order, negative terrain, and AI decisions; all pass. An early evaluation run shows the AI winning 99% of 100 games against a random opponent and 98% against a greedy opponent.

Remaining work
Graphs of win rate and score difference for the final presentation
Compare search depths (e.g., depth 4 vs. 6) for the tradeoff between win rate and run time
Possibly add more terrain maps or a larger grid
Tactical analysis: when and why the AI gives up negative terrain
Presentation slides (Dec 10)
Challenges
Full minimax on 24 lines is too slow, so we limited search depth and added alpha-beta pruning.
The extra-turn rule means players don't always alternate, so minimax had to check the current turn instead of assuming the players alternate.

Team contributions
Grace: Set up repository, initialized the different functions, utilized claude to get this up and running https://claude.ai/share/b2e5e945-9175-4eaf-875d-1cb88691911e. Set up the readme, board, evaluate, minimax, opponents, and play functions, helped with test_game.
Kate: made initial board design
Heipoe: Came up with the plan and ideas