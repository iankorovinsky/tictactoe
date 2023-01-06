"""
Tic Tac Toe Player
"""

import math
import copy

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

    number = 0

    for row in board:
        for cell in row:

            if cell == X:
                number = number+1
            elif cell == O:
                number = number-1
    if number % 2 == 0:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    i = 0
    for row in board:
        j = 0
        for cell in row:
            if cell == EMPTY:
                # Add current index
                possible_actions.add((i, j))
            j += 1
        i += 1
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    new_board = copy.deepcopy(board)

    character = player(board)

    if action not in actions(new_board):
        raise Exception

    new_board[action[0]][action[1]] = character

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == board[0][1] == board[0][2]:
        return board[0][0]
    elif board[1][0] == board[1][1] == board[1][2]:
        return board[1][0]
    elif board[2][0] == board[2][1] == board[2][2]:
        return board[2][0]
    elif board[0][0] == board[1][0] == board[2][0]:
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1]:
        return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2]:
        return board[0][2]
    elif board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    winner_of_board = winner(board)
    if winner_of_board == X or winner_of_board == O:
        return True

    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    winner_of_board = winner(board)

    if winner_of_board == X:
        return 1
    elif winner_of_board == O:
        return -1
    else:
        return 0


def minimax(board):
    if terminal(board):
        return None
    if player(board) == X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]


def max_value(board):
    temp_value = None
    optimal_move = None
    if terminal(board):
        return [utility(board), None]
    v = -math.inf
    for action in actions(board):
        temp_value = min_value(result(board, action))[0]
        if temp_value > v:
            v = temp_value
            optimal_move = action
            if temp_value == 1:
                return [v, optimal_move]

    return [v, optimal_move]


def min_value(board):
    temp_value = None
    optimal_move = None
    if terminal(board):
        return [utility(board), None]
    v = math.inf
    for action in actions(board):
        temp_value = max_value(result(board, action))[0]
        if temp_value < v:
            v = temp_value
            optimal_move = action
            if temp_value == -1:
                return [v, optimal_move]
    return [v, optimal_move]
