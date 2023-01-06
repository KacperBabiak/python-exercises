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
    x_number= 0
    o_number = 0
    for row in board:
        for space in row:
            if space == X:
                x_number= x_number+1
            elif space == O:
                o_number= o_number+1
                
    if o_number < x_number : return O
    else: return X 


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    actions_possible = set()
    i= 0 
    j = 0
    for row in board:
        for space in row:
            if space == EMPTY:
                actions_possible.add((i,j))
            j=j+1
        i=i+1
        j = 0
    return actions_possible


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action[0] <0 or action[0]> 2 or action[1] <0 or action[1] > 2:
        raise NameError('Invalid action' + str(action[0]) + str(action[1]))

    new_board = copy.deepcopy(board)
    symbol = player(new_board)

    new_board[action[0]][action[1]] = symbol

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    

    for i in range(0,2):
        #check horizontally
        if board[i][0] == board[i][1] == board[i][2]: return board[i][2]
        #check vertically
        if board[0][i] == board[1][i] == board[2][i]: return board[2][i]
    
    if board[0][0] == board[1][1] == board[2][2]: return board[2][2]
    if board[0][2] == board[1][1] == board[2][0]: return board[2][0]

    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board): return True

    for row in board:
        for space in row:
            if space == EMPTY:
               return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    player_won = winner(board)
    if player_won== X: return 1
    elif player_won  == O: return -1
    else: return 0 


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board): return True

    actions_possible = actions(board)
    player_active = player(board)
    best_action = None

    if player_active == X:
        max = -math.inf
        for action in actions_possible:
            if MinValue(result(board,action))>max:
                max = MinValue(result(board,action))
                best_action = action

    else:
        min = math.inf
        for action in actions_possible:
            if MaxValue(result(board,action))<min:
                min = MaxValue(result(board,action))
                best_action = action

    return best_action

def MaxValue(state):
    v = -math.inf
    if(terminal(state)):
        return utility(state)
    
    for action in actions(state):
        new_state = result(state,action)
        v = max(v,MinValue(new_state))

    return v

def MinValue(state):
    v = math.inf
    if(terminal(state)):
        return utility(state)
    
    for action in actions(state):
        new_state = result(state,action)
        v = min(v,MaxValue(new_state))
        
    return v