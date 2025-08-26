from system import System
from random import choice

class PlayerVsComputer(System):
    def __init__(self,p):
        super().__init__()
        self.running = True
        self.p = p
        self.c = 'MuazGPT'
        self.p_sym = 'X'
        self.c_sym = 'O'
        self.turn = self.p
        self.diff = 'easy'

    def choose_sym(self):
        self.pprint("Choose Your Symbol")
        while True:
            try:
                choice = input("Do you want to be X or O?: ").strip().upper()
                if choice in ['X', 'O']:
                    self.p_sym = choice
                    self.c_sym = 'O' if self.p_sym == 'X' else 'X'
                    self.turn = self.p if choice=='X' else self.c
                    break
            except:
                self.pprint("Invalid Input")

    def choose_diff(self):
        self.pprint("Choose Difficulty Level")
        print("1) Easy")
        print("2) Medium")
        print("3) Hard")

        while True:
            try:
                user = int(input(">>> "))
                if user==1:
                    self.diff='easy'
                    break
                if user==2:
                    self.diff='medium'
                    break
                if user==3:
                    self.diff='hard'
                    break

            except ValueError:
                self.pprint(f"Please Enter a Valid Integer!")

            except Exception as e:
                self.pprint(f"Error: {e}")

    def easy(self):
        moves = [i for i in self.board.keys() if self.board[i]=='-']
        if moves:
            move = choice(moves)
            self.board[move]=self.c_sym

    def medium(self):
        for i in self.board.keys():
            if self.board[i] == "-":
                self.board[i] = self.c_sym
                if self.is_win(self.c_sym):
                    return
                self.board[i] = "-"

        for i in self.board.keys():
            if self.board[i] == "-":
                self.board[i] = self.p_sym
                if self.is_win(self.p_sym):
                    self.board[i] = self.c_sym
                    return
                self.board[i] = "-"

        if self.board[5] == "-":
            self.board[5] = self.c_sym
            return

        self.easy()

    def hard(self):
        maxScore = -1000
        maxMove = 0

        for i in self.board.keys():
            if self.board[i]=="-":
                self.board[i]=self.c_sym
                score = self.minimax(False)
                self.board[i]="-"
                if score>maxScore:
                    maxScore=score
                    maxMove=i

        self.board[maxMove]=self.c_sym

    def minimax(self, isMax):
        if self.is_win(self.c_sym): return 1
        if self.is_win(self.p_sym): return -1
        if self.is_win()==False: return 0

        if isMax:
            maxScore = -1000

            for i in self.board.keys():
                if self.board[i]=="-":
                    self.board[i]=self.c_sym
                    score = self.minimax(False)
                    self.board[i]="-"
                    if score>maxScore:
                        maxScore=score

            return maxScore

        else:
            maxScore = 1000

            for i in self.board.keys():
                if self.board[i]=="-":
                    self.board[i]=self.p_sym
                    score = self.minimax(True)
                    self.board[i]="-"
                    if score<maxScore:
                        maxScore=score

            return maxScore

    def comp_move(self):
        if self.diff=="easy":
            self.easy()
        elif self.diff=="medium":
            self.medium()
        elif self.diff=="hard":
            self.hard()

    def system(self):
        self.choose_sym()
        self.choose_diff()

        self.pprint(f"You are {self.p_sym}, {self.c} is {self.c_sym}")
        self.pprint(f"Difficulty: {self.diff.title()}")

        while self.running:
            self.display(self.board)

            if self.turn == self.p:
                try:
                    user = int(input(f"{self.p}'s Turn: "))

                    if 1 <= user <= 9:
                        if self.board[user] != "-":
                            self.pprint("You can't take that position")
                        else:
                            self.board[user] = self.p_sym

                            if self.is_win(self.p_sym):
                                self.display(self.board)
                                self.pprint(f"{self.p} Won!")
                                self.running = False
                            elif self.is_win()==False:
                                self.display(self.board)
                                self.pprint("It's a Tie!")
                                self.running = False
                            else:
                                self.turn = self.c
                    else:
                        self.pprint("Please enter a number between 1-9!")

                except ValueError:
                    self.pprint("Please enter a valid integer!")

                except Exception as e:
                    self.pprint(f"Error: {e}")

            else:
                print(f"{self.c} is thinking...")
                self.comp_move()
 
                if self.is_win(self.c_sym):
                    self.display(self.board)
                    self.pprint(f"{self.c} Won!")
                    self.running = False

                elif self.is_win()==False:
                    self.display(self.board)
                    self.pprint("It's a Tie!")
                    self.running = False

                else:
                    self.turn = self.p
