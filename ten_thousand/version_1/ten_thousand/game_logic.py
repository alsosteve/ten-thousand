from random import randint
class GameLogic:

    @staticmethod
    def roll_dice(num_dice):
        return tuple(randint(1,6) for _ in range(0,num_dice))
        # or
        # return tuple(sample(range(1, 6 + 1), num_dice))

    @staticmethod
    def calculate_score(dice_list):
        score = 0
        straight = (1,2,3,4,5,6)
        checkstraight=[]
        pairs = 0

        for x in straight:        
            if straight.count(x) == dice_list.count(x): 
                checkstraight.append(x)
                print(checkstraight)
        if tuple(checkstraight) == straight:        
            score += 1500
            return score

        for x in range(7):
            if dice_list.count(x) == 2:
                pairs += 1
        if pairs == 3:
            score += 1500
            return score


        for x in range(2, 7):
            if dice_list.count(x) == 3:
                score += 100*x
            if dice_list.count(x) == 4:
                score += 200*x 
            if dice_list.count(x) == 5:
                score += 200*x+(x*100)
            if dice_list.count(x) == 6:
                score += 200*x+(x*200) 

        if 1 in dice_list:
            if dice_list.count(1) == 1:
                score += 100 
            if dice_list.count(1) == 2:
                score += 200
            if dice_list.count(1) == 3:
                score += 1000  
            if dice_list.count(1) == 4:
                score += 2000 
            if dice_list.count(1) == 5:
                score += 3000 
            if dice_list.count(1) == 6:
                score += 4000 

        if 5 in dice_list:
            if dice_list.count(5) == 1:
                score += 50 
            if dice_list.count(5) == 2:
                score += 100
        return score 
