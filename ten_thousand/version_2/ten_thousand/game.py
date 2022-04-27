from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker
import sys

class Game:
    
    def __init__(self):
        self.banker = Banker()
        self.scorer = GameLogic()

    def play(self, roller=GameLogic.roll_dice):

        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        response = input("> ")

        if response == "n":
            print("OK. Maybe another time")
            sys.exit()
        if response == "y":
            round_ = 0
            
            while True:
                keep_dice = []
                dice_count = 6
                round_ += 1

                print(f"Starting round {round_}")
                print(f"Rolling {dice_count} dice...")

                roll_result = roller(dice_count)
                roll_string = self.str_formatter(roll_result)
                print(f"*** {roll_string} ***")
                print("Enter dice to keep, or (q)uit:")
                
                keep_or_quit = input("> ")
                if keep_or_quit == "q":
                    print(f"Thanks for playing. You earned {self.banker.balance} points")
                    break
                for j in keep_or_quit:
                    if int(j) in roll_result:
                        keep_dice.append(int(j))
                        dice_count += -1
                unbanked_points = self.scorer.calculate_score(keep_dice)
                shelf_points = self.banker.shelf(unbanked_points)
                print(f"You have {self.banker.shelved} unbanked points and {dice_count} dice remaining")
                print('(r)oll again, (b)ank your points or (q)uit:') 
                r_b_q = input("> ")
                if r_b_q == "b":
                    banked_points = self.banker.bank()
                    print(f"You banked {banked_points} points in round {round_}")
                    print(f"Total score is {self.banker.balance} points")
                if r_b_q == "q":
                    print(f"Thanks for playing. You earned  {self.banker.balance} points")
                    break
        else:
            print ("Please select y or n")
              
    def str_formatter(self, string):
        stringify = str(string)
        final = stringify.replace(",", "").replace("[","").replace("]", "")
        return final


if __name__ == "__main__":
    game = Game()
    game.play()
