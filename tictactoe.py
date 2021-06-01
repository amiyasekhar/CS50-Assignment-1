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


def player(board): #works fine
    """
    Returns player who has the next turn on a board.
    """
    xcount = 0
    ocount = 0
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == X:
                xcount += 1
            elif board[i][j] == O:
                ocount += 1
    if xcount > ocount:
        return "O"
    else:
        return "X"

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                actions.append(tuple([i, j]))
    return actions



def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != None:
                print(board[i][j]," ", end = "")
            else:
                print(" ")
        print()
    print()



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = player(board)
    return result 
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    rowB = False
    collumnB = False
    diagonalB = False
    winner = None
    for row in board:
        res = all(elem == row[0] for elem in row) and row[0] != None
        if res:
            winner = row[0]
            break
    diagonalB = (board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0]) and board[1][1] != None
    if diagonalB:
        winner = board[1][1]
    count = 1
    cols = []
    marker = ""
    for collumn in range(len(board)):
        for row in range(len(board[0])):
            cols.append(board[row][collumn])
        if all(elem == cols[0] for elem in cols) and cols[0] != None:
            winner = cols[0]
            break
        else:
            cols = []
    return winner
    
            
            


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or (not any(EMPTY in sublist for sublist in board) and winner(board) is None)
    

                                             
def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == "X":
            return 1
        elif winner(board) == "O":
            return -1
        else:
            return 0
    #game hasn't finished
    return None

                                             
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == "X":
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move
def max_value(board):
    if terminal(board):
        return utility(board), None
    moves = actions(board)
    action = None
    util = float('-inf')
    for move in moves:
        res = result(board, move)
        if utility(board) == None:
            value, adv = min_value(res)
            if value > util:
                util = value
                action = move
        else:
            util = utility(board)
            action = move
    return util, action

def min_value(board):
    if terminal(board):
        return utility(board), None
    moves = actions(board)
    action = None
    util = float('inf')
    for move in moves:
        res = result(board, move)
        if utility(board) == None:
            value, adv = max_value(res)
            if value < util:
                util = value
                action = move
        else:
            util = utility(board)
            action = move
    return util, action
        
        
    
    
                        
            
                    
        
