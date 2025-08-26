from system import System

class Tutorial(System):
    def __init__(self):
        super().__init__()
        self.current_player = 'X'

    def wait(self, message="Press Enter to continue..."):
        input(f"\n{message}")
 
    def display_position_board(self):
        position_board = {i: str(i) for i in range(1, 10)}
        print("\nPosition numbers:")
        self.display(position_board)

    def create_custom_board(self, positions):
        custom_board = {i: '-' for i in range(1, 10)}
        for pos, symbol in positions.items():
            custom_board[pos] = symbol
        return custom_board
 
    def display_custom_board(self, positions):
        board = self.create_custom_board(positions)
        self.display(board)

    def system(self):
        self.clear()

        self.pprint("WELCOME TO TIC-TAC-TOE TUTORIAL")
        print("Learn to master the classic strategy game!")
        print("This interactive tutorial will guide you step by step.")
        print("Press Enter after reading each section to continue.")
        self.wait()
 
        self.clear()
        self.pprint("WHAT IS TIC-TAC-TOE?")
        print("Tic-Tac-Toe (also known as 'Noughts and Crosses') is a classic")
        print("strategy game played on a 3×3 grid. Two players take turns marking")
        print("spaces with their symbol (X or O) with the goal of getting three")
        print("of their marks in a row.")
        self.wait()

        self.clear()
        self.pprint("GAME SETUP")
        print("THE GRID: The game is played on a 3×3 grid, creating 9 empty spaces:")
        self.display(self.board)
        print("\nPLAYERS:")
        print("• Player 1: Uses X symbols")
        print("• Player 2: Uses O symbols")
        print("\nTURN ORDER: Player X always goes first!")
        self.wait()
 
        self.clear()
        self.pprint("BASIC RULES")
        print("1. TAKE TURNS: Players alternate placing their symbols")
        print("2. ONE SYMBOL PER TURN: Each turn, place exactly one X or O")
        print("3. NO OVERWRITING: Once a space is filled, it cannot be changed")
        print("4. WIN OR DRAW: The game ends when someone wins or all spaces are filled")
        self.wait()

        self.clear()
        self.pprint("HOW TO PLAY: STEP-BY-STEP")
        print("STEP 1: Choose Your Space")
        print("On your turn, select any empty space on the grid.")
        print("Spaces are numbered 1-9 for reference:")
        self.display_position_board()
        self.wait("Press Enter to see the next step...")

        print("\nSTEP 2: Place Your Symbol")
        print("Select your chosen space to place your symbol (X or O).")
        self.wait("Press Enter to see the next step...")

        print("\nSTEP 3: Check for a Win")
        print("After each move, check if you've achieved three in a row.")
        self.wait("Press Enter to see the next step...")
 
        print("\nSTEP 4: Pass the Turn")
        print("If no one has won and spaces remain, the other player takes their turn.")
        self.wait()

        self.clear()
        self.pprint("WINNING CONDITIONS")
        print("You win by getting THREE OF YOUR SYMBOLS IN A ROW.")
        print("This can be achieved in 8 different ways:")

        print("\nHORIZONTAL WINS (3 ways):")
        print("Top row:")
        self.display_custom_board({1: 'X', 2: 'X', 3: 'X'})
        self.wait("Press Enter to continue...")
 
        print("Middle row:")
        self.display_custom_board({4: 'X', 5: 'X', 6: 'X'})
        self.wait("Press Enter to continue...")

        print("Bottom row:")
        self.display_custom_board({7: 'X', 8: 'X', 9: 'X'})
        self.wait("Press Enter to continue...")

        self.clear()
        print("\nVERTICAL WINS (3 ways):")
        print("Left column:")
        self.display_custom_board({1: 'X', 4: 'X', 7: 'X'})
        self.wait("Press Enter to continue...")

        print("Middle column:")
        self.display_custom_board({2: 'X', 5: 'X', 8: 'X'})
        self.wait("Press Enter to continue...")

        print("Right column:")
        self.display_custom_board({3: 'X', 6: 'X', 9: 'X'})
        self.wait("Press Enter to continue...")
 
        self.clear()
        print("\nDIAGONAL WINS (2 ways):")
        print("Main diagonal:")
        self.display_custom_board({1: 'X', 5: 'X', 9: 'X'})
        self.wait("Press Enter to continue...")

        print("Anti-diagonal:")
        self.display_custom_board({3: 'X', 5: 'X', 7: 'X'})
        self.wait()

        self.clear()
        self.example_game_1()
        self.example_game_2()
 
        self.clear()
        self.pprint("STRATEGY TIPS")
        print("OPENING MOVES:")
        print("• BEST first move: Center (position 5) - gives you the most winning opportunities")
        print("• SECOND BEST: Any corner (positions 1, 3, 7, 9)")
        print("• AVOID: Edges (positions 2, 4, 6, 8) as your opening move")
        self.wait("Press Enter to see key strategies...")

        print("\nKEY STRATEGIES:")
        print("1. WIN WHEN YOU CAN: Always take a winning move if available")
        print("2. BLOCK YOUR OPPONENT: If they have two in a row, block the third space")
        print("3. CREATE MULTIPLE THREATS: Try to set up two ways to win at once")
        print("4. CONTROL THE CENTER: The center space is part of 4 different winning lines")
        print("5. USE CORNERS: Corners are part of 3 different winning lines each")
        self.wait("Press Enter to see advanced tactics...")

        self.clear()
        self.pprint("ADVANCED TACTICS:")
        print("THE FORK: Create two ways to win simultaneously")
        print("Example:")
        self.display_custom_board({1: 'X', 5: 'X', 3: 'O', 7: 'O'})
        print("If X plays position 9, they create two winning threats!")
        self.wait()

        self.clear()
        self.pprint("COMMON BEGINNER MISTAKES")
        print("• NOT BLOCKING OBVIOUS WINS: Always check if your opponent can win on their next turn")
        print("• PLAYING RANDOMLY: Have a plan, don't just fill empty spaces")
        print("• IGNORING THE CENTER: The center space is the most valuable")
        print("• NOT LOOKING FOR FORKS: Missing opportunities to create multiple winning threats")
        self.wait()
 
        self.clear()
        self.practice_challenges()
 
        self.clear()
        self.pprint("CONGRATULATIONS!")
        print("You've completed the Tic-Tac-Toe tutorial!")
        print("\nRemember:")
        print("• Think ahead: Consider your opponent's next move")
        print("• Stay alert: Always check for immediate wins and blocks")
        print("• Practice strategy: The more you play, the better you'll recognize patterns")
        print("• Have fun: It's a game - enjoy the mental challenge!")
        print("\nStart with the center, watch for winning opportunities,")
        print("and may the best strategist win!")

        self.wait("Press Enter to finish the tutorial...")
        print("\nThank you for completing the Tic-Tac-Toe Tutorial!")
        print("You're now ready to play like a pro!")

    def example_game_1(self):
        self.pprint("EXAMPLE GAME 1: Quick Win")
        print("Let's watch a game step by step:")
 
        print("\nTurn 1 - X plays top-left (position 1):")
        self.display_custom_board({1: 'X'})
        self.wait("Press Enter to see Turn 2...")

        print("\nTurn 2 - O plays center (position 5):")
        self.display_custom_board({1: 'X', 5: 'O'})
        self.wait("Press Enter to see Turn 3...")

        print("\nTurn 3 - X plays bottom-right (position 9):")
        self.display_custom_board({1: 'X', 5: 'O', 9:'X'})
        self.wait("Press Enter to see Turn 4...")

        print("\nTurn 4 - O plays bottom-left (position 7):")
        self.display_custom_board({1: 'X', 5: 'O', 9:'X', 7: 'O'})
        self.wait("Press Enter to see Turn 5...")

        print("\nTurn 5 - X plays top-right (position 3):")
        self.display_custom_board({1: 'X', 5: 'O', 9:'X', 7: 'O', 3: 'X'})
        self.wait("Press Enter to see Turn 6...")

        print("\nTurn 6 - O blocks with top-center (position 2):")
        self.display_custom_board({1: 'X', 5: 'O', 9:'X', 7: 'O', 3: 'X', 2: 'O'})
        self.wait("Press Enter to see the winning move...")

        print("\nTurn 7 - X wins with center-right (position 6):")
        self.display_custom_board({1: 'X', 5: 'O', 9:'X', 7: 'O', 3: 'X', 2: 'O', 6: 'X'})
        self.pprint("X WINS WITH A VERTICAL!")
        self.wait()
        self.clear()
 
    def example_game_2(self):
        self.pprint("EXAMPLE GAME 2: Draw Game")
        print("Here's how a game might end in a draw:")
        self.display_custom_board({1: 'X', 2: 'O', 3: 'X', 4: 'O', 5: 'O', 6: 'X', 7: 'O', 8: 'X', 9: 'O'})
        print("\nNo three in a row = DRAW/TIE GAME")
        self.wait()
 
    def practice_challenges(self):
        self.pprint("PRACTICE CHALLENGES")
        print("Test your skills with these scenarios!")

        print("\nCHALLENGE 1: It's your turn as X. Can you win in one move?")
        self.display_custom_board({1: 'X', 2: 'O', 5: 'X', 6: 'O'})
        answer = input("\nWhich position should X play to win? (1-9): ")
        if answer == '9':
            print("CORRECT! Position 9 creates a diagonal win!")
            self.display_custom_board({1: 'X', 2: 'O', 5: 'X', 6: 'O', 9: 'X'})
        else:
            print("Not quite! The answer is position 9 for a diagonal win.")
            self.display_custom_board({1: 'X', 2: 'O', 5: 'X', 6: 'O', 9: 'X'})
        self.wait("Press Enter for Challenge 2...")

        print("\nCHALLENGE 2: You're O. Your opponent threatens to win. Where must you play?")
        self.display_custom_board({1: 'X', 3: 'X', 5: 'O'})
        answer = input("\nWhich position should O play to block X's win? (1-9): ")
        if answer == '2':
            print("CORRECT! Position 2 blocks the horizontal win!")
            self.display_custom_board({1: 'X', 2: 'O', 3: 'X', 5: 'O'})
        else:
            print("Not quite! The answer is position 2 to block the top row.")
            self.display_custom_board({1: 'X', 2: 'O', 3: 'X', 5: 'O'})
        self.wait("Press Enter for Challenge 3...")
 
        print("\nCHALLENGE 3: You're X. Can you create a winning fork?")
        self.display_custom_board({1: 'X', 5: 'O'})
        answer = input("\nWhich position creates the best fork for X? (1-9): ")
        if answer == '9':
            print("EXCELLENT! Position 9 creates multiple winning threats!")
            self.display_custom_board({1: 'X', 5: 'O', 9: 'X'})
            print("Now X threatens to win with either 3-5-7 diagonal or 7-8-9 bottom row!")
        else:
            print("Good try! Position 9 would create the best fork.")
            self.display_custom_board({1: 'X', 5: 'O', 9: 'X'})
            print("This creates multiple winning threats!")
        self.wait()
