# minimax.py
# The AI: minimax search with alpha-beta pruning.
# The AI is always "A" (maximizer). The other side is always "P" (minimizer).


def evaluate(board):
    # How good is this board for the AI? Its score minus the opponent's score.
    return board.scores["A"] - board.scores["P"]


def minimax(board, depth, alpha, beta):
    # Returns (best value, best move) looking `depth` moves ahead.
    # alpha = best value the AI is already guaranteed somewhere higher in the tree.
    # beta  = best (lowest) value the opponent is already guaranteed.

    # Stop searching if we hit the depth limit or the game is over.
    if depth == 0 or board.is_over():
        return evaluate(board), None

    best_move = None

    if board.turn == "A":
        # AI's turn: pick the move with the HIGHEST value.
        best = float("-inf")
        for move in board.available_moves():
            child = board.copy()
            child.make_move(move)
            # child.turn is still "A" if the AI finished a box (extra turn).
            value, _ = minimax(child, depth - 1, alpha, beta)
            if value > best:
                best = value
                best_move = move
            alpha = max(alpha, best)
            if alpha >= beta:
                break       # prune: the opponent would never let us get here
    else:
        # Opponent's turn: assume they pick the move with the LOWEST value.
        best = float("inf")
        for move in board.available_moves():
            child = board.copy()
            child.make_move(move)
            value, _ = minimax(child, depth - 1, alpha, beta)
            if value < best:
                best = value
                best_move = move
            beta = min(beta, best)
            if alpha >= beta:
                break       # prune: the AI would never let us get here

    return best, best_move


def ai_move(board, depth=4):
    # Start with the widest possible alpha/beta window.
    _, move = minimax(board, depth, float("-inf"), float("inf"))
    return move