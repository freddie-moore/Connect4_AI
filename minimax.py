from copy import deepcopy
#simulate all possible moves in current game state
def getAllMoves(anBoard):
    moves = []
    for move in range(7):
        tempBoard = deepcopy(anBoard)
        if tempBoard.moveMade(move)[0]:
            tempBoard.bestCol = move
            moves.append(tempBoard)

    return moves

#minimax algo
def minimax(position, depth, alpha, beta, max_player):
    if depth == 0 or position.draw == True or position.win == True:
        return position.evalBoard(), position

    if max_player:
        maxEval = float('-inf')
        best_move = None

        for move in getAllMoves(position):
            evaluation = minimax(move, depth - 1, alpha, beta, False)[0]
            if maxEval < evaluation:
                best_move = move
                maxEval = evaluation

            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break

        return maxEval, best_move
    else:
        minEval = float('+inf')
        best_move = None
        for move in getAllMoves(position):
            evaluation = minimax(move, depth - 1, alpha, beta, True)[0]
            if minEval > evaluation:
                best_move = move
                minEval = evaluation

            beta = min(beta, evaluation)
            if beta <= alpha:
                break

        return minEval, best_move