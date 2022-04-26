from random import randint
class GameLogic:


    def roll_dice(num_dice):
        return tuple(randint(1,6) for _ in range(0,num_dice))
        # or
        # return tuple(sample(range(1, 6 + 1), num_dice))

    @staticmethod
    def calculate_score(dice_list):
        score = 0
        if 1 in dice_list:
            return "yes"

    '''
    def calculate_score(dice_list):
        total = 0
        for item in score:
            times = score.count(item)
            if times == 2:
                if item == 1:
                    total += 200
                if item == 5:
                    total += 100
            if times == 1:
                if item == 1:
                    total += 100
                if item == 5:
                    total += 50
        return total
    '''