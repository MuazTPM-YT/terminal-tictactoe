from system import System 

class PlayerVsPlayer(System):
    def __init__(self, p1, p2):
        super().__init__()
        self.running = True
        self.turns = []
        self.p1 = p1 if len(p1)<=30 else p1[:30]+"..."
        self.p2 = p2 if len(p2)<=30 else p2[:30]+"..."
        self.turn = self.p1
        self.p1_sym = "X"
        self.p2_sym = "O"

    def system(self):
        while self.running:
            self.display(self.board)
            try:
                self.user = int(input(f"{self.turn}'s Turn: "))

                if self.user>=1 and self.user<=9:
                    if self.turn==self.p1:
                        if self.board[self.user]!="-":
                            self.pprint(f"{self.turn} can't take that position")
                        else:
                            self.board[self.user]=self.p1_sym

                            if self.is_win(self.p1_sym):
                                self.display(self.board)
                                self.pprint(f"{self.turn} Won!")
                                self.running = False

                            if self.is_win(self.p1_sym)==False:
                                self.display(self.board)
                                self.pprint("It's a Tie!")
                                self.running = False

                            self.turns.append(self.user)
                            self.turn = self.p2

                    elif self.turn==self.p2:
                        if self.board[self.user]!="-":
                            self.pprint(f"{self.turn} can't take that position")
                        else:
                            self.board[self.user]=self.p2_sym

                            if self.is_win(self.p2_sym):
                                self.display(self.board)
                                self.pprint(f"{self.turn} Won!")
                                self.running = False

                            if self.is_win(self.p2_sym)==False:
                                self.display(self.board)
                                self.pprint("It's a Tie!")
                                self.running = False

                            self.turns.append(self.user)
                            self.turn = self.p1

                    else:
                        self.pprint("Unknown Player!")

                else:
                    self.pprint("Please Enter a Number Between 1-9!")

            except ValueError:
                self.pprint(f"Please Enter a Valid Integer!")

            except Exception as e:
                self.pprint(f"Error: {e}")
