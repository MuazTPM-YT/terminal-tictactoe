from pvp import PlayerVsPlayer
from pvc import PlayerVsComputer
from tutorial import Tutorial
from system import System

from sys import exit
from time import sleep

class TicTacToe(System):
    def intro(self):
        self.pprint("Welcome To Muaz's TicTacToe Game!")
        print(f"What would you like to do?")
        print(f"1) Player vs Player")
        print(f"2) Player vs Computer")
        print(f"3) Tutorial")
        print(f"4) Quit")

    def refresh(self):
        sleep(3)
        self.clear()
        self.intro()

    def main(self):
        self.intro()
        while True:
            try:
                choice = int(input(">>> ").strip())

                if choice==1:
                    p1 = input("Player 1 (X): ").title()
                    p2 = input("Player 2 (O): ").title()
                    PlayerVsPlayer(p1, p2).system()
                    self.refresh()

                elif choice==2:
                    p = input("Player Name: ")
                    PlayerVsComputer(p).system()
                    self.refresh()

                elif choice==3:
                    Tutorial().system()
                    self.refresh()

                elif choice==4:
                    self.pprint("Thank You For Playing!")
                    sleep(3)
                    exit(0)
                else:
                    self.pprint(f"Invalid Option!")

            except ValueError:
                self.pprint(f"Please Enter a Valid Integer!")

            except Exception as e:
                self.pprint(f"Error: {e}")

if __name__ == "__main__":
    TicTacToe().main()
