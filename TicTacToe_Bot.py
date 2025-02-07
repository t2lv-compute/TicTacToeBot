import random
import math
import pygame # type: ignore

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

def check_win(code):
    if not type(code) is list or len(code)<9:
        raise ValueError("ERROR: CODE IS EITHER TOO SHORT OR NOT A LIST")
    # horizontal
    if code[0] == code[1] and code[1] == code[2]:
        return f"{code[0]} Win"
    if code[3] == code[4] and code[4] == code[5]:
        return f"{code[3]} Win"
    if code[6] == code[7] and code[7] == code[8]:
        return f"{code[6]} Win"
    # vertical
    if code[0] == code[3] and code[3] == code[6]:
        return f"{code[0]} Win"
    if code[1] == code[4] and code[4] == code[7]:
        return f"{code[1]} Win"
    if code[2] == code[5] and code[5] == code[8]:
        return f"{code[2]} Win"
    # diagonal
    if code[0] == code[4] == code[8]:
        return f"{code[0]} Win"
    if code[2] == code[4] == code[6]:
        return f"{code[2]} Win"
    return "continue"

def render_board(code=[" "," "," "," "," "," "," "," "," "]):
    if not type(code) is list or len(code)<9:
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
    #board.insert(-1,"\n")
    #print(board)
    board = "".join(board)
    print(board)
    return board

#render_board(["X","X","O","O","O","X","X","O","X"])
#check_win(1)
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

bot = machinelearning_TicTacToe("TobAI")

print("Welcome to TicTacToe!")
opponent = input("Press 1 to play against a human and 2 to play against AI.\n    >>> ")
if None:
    pass
else:
    current_board = ["1","2","3","4","5","6","7","8","9"]
    print("GAME START!")
    player = "X"
    move = "pass"
    while True:
        while move == "pass" or current_board[int(move)-1].isalpha():
            move = input(f"Player {player}'s Turn\n\nEnter your move, by square. If you have already done so, you may be trying to overwrite an existing move. (1-9):\n    >>> ")
        if player == "X":
            current_board[int(move)-1]="X"
            player = "O"
        else: 
            current_board[int(move)-1]="O"
            player = "X"
        if "Win" in check_win(current_board).split():
            print()
            print(check_win(current_board)+"!")
            #print()
            render_board(current_board)
            break