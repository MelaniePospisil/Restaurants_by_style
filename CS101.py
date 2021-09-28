import sys
script_name = sys.argv[0]

class TikTakToe:
    def __init__(self):
        self.field = ["(1)", "(2)", "(3)", "(4)", "(5)", "(6)", "(7)", "(8)", "(9)"]
        self.turn = " X "
        self.already_taken = []
        print(" ")
        print("Welcome to tictactoe")
        print(" ")
        print("Adress the squares with the following numbers:")
        print(" ")
        print("[1][2][3]")
        print("[4][5][6]")
        print("[7][8][9]")
        print("  ")
        print("It's " + self.turn +"'s turn")
        print(" ")
        cell = int(input("Okay my dear " + self.turn + ", which cell do you want? "))
        self.set(cell)
        print(" ")
        


    def print_game(self):
        print("-------------------------")
        print("")
        print(self.field[0] + "  I  " + self.field[1] + "  I  " + self.field[2])
        print("")
        print("-------------------")
        print("")
        print(self.field[3] + "  I  " + self.field[4] + "  I  " + self.field[5])
        print("")
        print("-------------------")
        print("")
        print(self.field[6] + "  I  " + self.field[7] + "  I  " + self.field[8])

    def set(self, num):
        if num in self.already_taken or num<1 or num>9:
            print("-------------------------")
            print("  ")
            print("This is already taken, stupid. Try another one.")
            print("  ")
        else:
            self.already_taken.append(num)
            self.field[num-1] = self.turn
            if self.turn == " X ":
                self.turn = " O "
            else:
                self.turn = " X "
            self.print_game()
            print("  ")
        #Check, if game is already won
        if self.check_for_win() != "no":
            print("STOP! " + self.check_for_win() + " won! Wohooooooo")
        else:
            print("It's " + self.turn +"'s turn")
            print(" ")
            cell = int(input("So my dear " + self.turn + ", which cell do you want? "))
            self.set(cell)
            print(" ")

    def check_for_win(self):
        winning_lines = [[1,2,3], [1,5,9], [1,4,7], [2,5,8], [4,5,6], [3,6,9], [3,5,7]]
        for line in winning_lines:
            if self.field[line[0]-1] == self.field[line[1]-1] and self.field[line[0]-1] == self.field[line[2]-1]:
                return self.field[line[0]]
        return "no"
    
game_1 = TikTakToe()

    



