import os

class System:
    def __init__(self):
        self.board = {
            1: '-', 2: '-', 3: '-',
            4: '-', 5: '-', 6: '-',
            7: '-', 8: '-', 9: '-',
        }

    def display(self, board):
        for i in range(1,8,3):
            print(f"{board[i]} | {board[i+1]} | {board[i+2]}")

    def is_win(self, player=None):
        if self.board[1] == self.board[2] == self.board[3] == player != "-": return True
        if self.board[4] == self.board[5] == self.board[6] == player != "-": return True
        if self.board[7] == self.board[8] == self.board[9] == player != "-": return True
        if self.board[1] == self.board[4] == self.board[7] == player != "-": return True
        if self.board[2] == self.board[5] == self.board[8] == player != "-": return True
        if self.board[3] == self.board[6] == self.board[9] == player != "-": return True
        if self.board[1] == self.board[5] == self.board[9] == player != "-": return True 
        if self.board[3] == self.board[5] == self.board[7] == player != "-": return True
        if "-" not in self.board.values(): return False

    def pprint(self, words):
        print("-"*50)
        print(words.center(50))
        print("-"*50)

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
