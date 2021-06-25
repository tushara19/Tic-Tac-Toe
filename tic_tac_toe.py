import copy

EMPTY = None
X = 'x'
O = 'o'

def initial_state():
    return [[EMPTY] * 3, [EMPTY] * 3, [EMPTY] * 3]             #[[X,       X,      O]
                                                                # [EMPTY,   O,      X]]
                                                                # [O,       EMPTY, EMPTY]
def player(board):
    """returns the player that has to make the move"""

    one_row_board = [x_or_o for row in board for x_or_o in row]
    if one_row_board.count(X) > one_row_board.count(O):
    	return O
    return X

def actions(board):
    """returns all possible moves that can be made on the board """

    possible_acts =[(i,j) for i in range(0,3) for j in range(0,3) if board[i][j] == EMPTY] 
    return possible_acts

def result(board, action):
    """ returns the board state when the action is made """

    boardtemp = copy.deepcopy(board)
    x, y = action
    if board[x][y] != EMPTY:
        raise IndexError
    else:
        cur = player(board)
        boardtemp[x][y] = cur
    return boardtemp

def winner(board):
    """ Returns the winner of the game, if there is one. """

    #checking each row of board
    for sub in board:
    	if all([ele == sub[0] for ele in sub]):
    		return sub[0]
    
    #transpose for easy checking if there's a win column wise		
    transpose = [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))] 
    for row in transpose:
    	if all([ele == row[0] for ele in row]):
    		return row[0]
	
    #principal diagonal
    diag =[board[i][j] for i in range(0,3) for j in range(0,3) if i == j]
    if all([ele == diag[0] for ele in diag]):
    		return diag[0]

    #second diagonal right to left		
    if board[2][0] == board[1][1] and board[1][1] == board[0][2]:
        return board[1][1]
        
    #Match draw situation
    l1 = [(i,j) for i in range(0,3) for j in range(0,3) if board[i][j] != EMPTY]
    if len(l1) == 9:
        return "No one"

def terminal(board):
    """ Returns True if game is over, False otherwise. """

    return winner(board) == X or winner(board) == O or winner(board) == "No one"

def utility(board):
    """ Returns 1 if X has won the game, -1 if O has won, 0 otherwise. """

    if terminal(board) == True:
        if winner(board) == X:
            return 1
        if winner(board) == O:
            return -1
        else:
            return 0

""" Using minimax algorithm to determine best/optimal move for computer"""

def Max(board):
	if terminal(board):
		return utility(board)
	else:
		opt = float('-inf')
		for action in actions(board):
			opt = max(opt, Mini(result(board, action)) )
		return opt

def Mini(board):
	if terminal(board):
		return utility(board)
	else:
		opt = float('inf')
		for action in actions(board):
			opt = min(opt, Max(result(board, action)))
		return opt

def minimax(board):
    cur_player = player(board)
    if cur_player == X:
        v = float('-inf')
        for action in actions(board):
            res = Mini(result(board, action))
            if res > v:
                v = res
                best_move = action
    else:
        v = float('inf')
        for action in actions(board):
            res = Max(result(board, action))
            if res < v:
                v = res
                best_move = action
    return best_move

    

