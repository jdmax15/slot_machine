import os
import emoji
import random

#comment for commit

class Slot_Machine:
    def __init__(self, total):
        self.total = total
        self.spin_result = self.spin()
        
        
    def make_board(self, r1, r2, r3):
        print(f"           Total Money: {self.total}")
        print(f"")
        print(f"=========== SLOT MACHINE =============")
        print(f"")
        print(f"======  {r1}  =====  {r2}  =====  {r3}  =======")
        print(f"")
        print(f"======================================")


    def spin(self):
        emoji_dict = {
            1: emoji.emojize(':butterfly:'),
            2: emoji.emojize(':cherries:')
        }
        
        result_1 = random.choice(list(emoji_dict.values()))
        result_2 = random.choice(list(emoji_dict.values()))
        result_3 = random.choice(list(emoji_dict.values()))

        return result_1, result_2, result_3
    
    def set_bet_and_spin(self, bet):
        self.total -= bet
        os.system('clear')
        r1, r2, r3 = self.spin()              
        if r1 == r2 and r1 == r3:
            self.total += bet * 5
        self.make_board(r1, r2, r3)   

# GettingUnboundLocalError with start_money
def main():
    try:
        start_money = input(int("Enter your starting money: "))
    except ValueError:
        print("Please only enter a number.")

    slots = Slot_Machine(start_money)
    
    while True:
        try:
            choice = int(input("Type amount to bet (1-5). "))
            if choice not in list(range(1, 5)):
                raise ValueError()
            slots.set_bet_and_spin(choice)

        except ValueError:
            print("Please only enter 1-5.")


if __name__ == "__main__":
    main()