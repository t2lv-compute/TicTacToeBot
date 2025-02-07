import random
import math

class machinelearning_TicTacToe ():
    def __init__(self, name):
        self.reset(name)
    def train(self):
        self.boards[1,2,3,4,5,6,7,8,9] = []
        for i in range(0,9):
            for _ in range(0,10):
                self.boards[1,2,3,4,5,6,7,8,9].append(i+1)
        print(self.boards)
    def make_move(self, board_pos):
        if board_pos in self.boards:
            return random.choice(self.boards[board_pos])
        else:
            return None #  code here that just returns a random position
    def reset(self,name):
        #self.boards: dict -- ex: [1,2,"x",3,"o",4,5,6,7]:[1,1,1,1,2,2,3,3,3,4,4,4,4,4,4,5,5,5,6,6,6,6,6,6,7]
        self.boards = {}
        self.name = name

def render_board(code=[" "," "," "," "," "," "," "," "," "]):
    if len(code)<9 or not type(code) is list:
        return "ERROR: CODE IS EITHER TOO SHORT OR NOT A LIST"
    board = []
    for i in range(0,len(code)*4,4):
        board.insert(i," ")
        board.insert(i+1,code[int(i/4)])
        board.insert(i+2," ")
        if (i+3)%12==11:
            board.insert(i+3,"\n")
        else: 
            board.insert(i+3,"|")
        #print((i+3)%12==11)
    #print(i)
    board.insert(0,"\n")
    board.insert(13,"---|---|---\n")
    board.insert(26,"---|---|---\n")
    board.insert(-1,"\n")
    #print(board)
    board = "".join(board)
    print(board)
    return board

#render_board(["X","X","O","O","O","X","X","O","X"])
bot = machinelearning_TicTacToe("TobAI")

print("Welcome to TicTacToe!")
opponent = input("Press 1 to play against a human and 2 to play against AI.\n    >>> ")
if None:
    pass
else:
    current_board = [" "," "," "," "," "," "," "," "," "]
    print("GAME START!")
    while True:
        render_board(current_board)
        move = input("Enter your move (1-9):\n    >>> ")