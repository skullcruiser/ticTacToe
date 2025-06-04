"""
Tic Tac Toe Player
"""
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    ocount = 0  # number of moves by o
    xcount = 0  # number of moves by x
    # loop to reach each square and find ocount and xcount
    for i in range(3):
        for j in range(3):
            if (board[i][j] == X):
                xcount += 1
            elif (board[i][j] == O):
                ocount += 1
    if (ocount == xcount):  # first move is of x , x has higher or equal moves to o
        return X
    else: 
        return O
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # all permuatations of actions
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # given action
    row, col = action

    # out of bounds checking
    if (row < 0 or col < 0 or row > 2 or col > 2):
        raise Exception("Invalid move due to out of bounds.")

    # checking if any square on which action is to be performed is already not empty
    if (board[row][col] != EMPTY):
        raise Exception("Given action is already done before.")
    
    # deep copy
    outer = []
    for i in range(3):
        inner = []
        for j in range(3):
            inner.append(board[i][j])
        outer.append(inner)

    outer[row][col] = player(outer)
    return outer

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # diagonals
    if (board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY):
        return board[0][0]
    elif (board[2][0] == board[1][1] == board[0][2] and board[0][2] != EMPTY):
        return board[2][0]
    for i in range(3):
        # rows
        if (board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY):
            return board[i][0]
        # columns
        elif (board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY):
            return board[0][i]
    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if the game is over, False otherwise.
    """
    if winner(board) is not None:  # If there is a winner, the game is over
        return True
    
    # If no winner, check if the board is full (tie game)
    for row in board:
        if EMPTY in row:  # There are still empty spaces, game is not over
            return False
    return True
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (winner(board) == X): 
        return 1
    elif (winner(board) == O): 
        return -1
    else: 
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if (terminal(board)): 
        return None

    if player(board) == X:
        best_score = -math.inf
        best_move = None
        for action in actions(board):
            new_board = result(board, action)
            score = minimax_score(new_board)
            if score > best_score:
                best_score = score
                best_move = action
        return best_move
    else:
        best_score = math.inf
        best_move = None
        for action in actions(board):
            new_board = result(board, action)
            score = minimax_score(new_board)
            if score < best_score:
                best_score = score
                best_move = action
        return best_move


def minimax_score(board):
    """
    Returns the score of the board from the perspective of the current player.
    """
    if terminal(board):
        return utility(board)

    if player(board) == X:
        best_score = -math.inf
        for action in actions(board):
            new_board = result(board, action)
            score = minimax_score(new_board)
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for action in actions(board):
            new_board = result(board, action)
            score = minimax_score(new_board)
            best_score = min(score, best_score)
        return best_score