from ten_thousand.game_logic import GameLogic
from ten_thousand.banker import Banker
import sys


class Game:

    def __init__(self):
        self.banker = Banker()
        self.scorer = GameLogic()
        self.roller = None
        self.round_ = 0
        self.dice_count = 0

    def play(self, roller=GameLogic.roll_dice):
        self.roller = roller
        print("Welcome to Ten Thousand")
        print("(y)es to play or (n)o to decline")
        response = input("> ")

        if response == "n":
            print("OK. Maybe another time")
            sys.exit()
        if response == "y":

            while True:
                self.dice_count = 6
                self.round_ += 1
                print(f"Starting round {self.round_}")
                self.play_round()
    
    def play_round(self):
            print(f"Rolling {self.dice_count} dice...")
            roll_result = self.roller(self.dice_count)
            roll_string = self.str_formatter(roll_result)
            print(f"*** {roll_string} ***")                     
            print("Enter dice to keep, or (q)uit:")

            keep_or_quit = input("> ")
            if keep_or_quit == "q":
                print(f"Thanks for playing. You earned {self.banker.balance} points")
                sys.exit()
            else:
                keep_dice = []
                for j in keep_or_quit:
                    keep_dice.append(int(j))
                self.dice_count -= len(keep_dice)
                self.banker.shelf(self.scorer.calculate_score(keep_dice))
                print(f"You have {self.banker.shelved} unbanked points and {self.dice_count} dice remaining")
                print('(r)oll again, (b)ank your points or (q)uit:') 
            r_b_q = input("> ")
            if r_b_q == "r":
                self.play_round()
            if r_b_q == "b":
                banked_points = self.banker.bank()
                print(f"You banked {banked_points} points in round {self.round_}")
                print(f"Total score is {self.banker.balance} points")
            if r_b_q == "q":
                print(f"Thanks for playing. You earned  {self.banker.balance} points")
                sys.exit()
              
    def str_formatter(self, string):
        stringify = str(string)
        final = stringify.replace(",", "").replace("[","").replace("]", "")
        return final


if __name__ == "__main__":
    game = Game()
    game.play()
