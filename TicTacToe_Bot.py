import random

class machinelearning_TicTacToe ():
    def __init__(self):
        #self.boards: dict -- ex: [1,2,"x",3,"o",4,5,6,7]:[1,1,1,1,2,2,3,3,3,4,4,4,4,4,4,5,5,5,6,6,6,6,6,6,7]
        self.boards = {}
        self.boards[1,2,3,4,5,6,7,8,9] = []
        for i in range(0,9):
            for _ in range(0,10):
                self.boards[1,2,3,4,5,6,7,8,9].append(i+1)
        print(self.boards)

def render_board(code):
    board = '    |    |    \n____|____|____\n    |    |    \n____|____|____\n    |    |    \n    |    |    '
    if len(code)<9 or not type(code) is list:
        return "ERROR: CODE IS EITHER TOO SHORT OR NOT A LIST"
    board[2]=code[0]
    board[6]=code[1]
    print(board)
    return board

render_board(["X","O"," "," "," "," "," "," "," "," "])
bot = machinelearning_TicTacToe()