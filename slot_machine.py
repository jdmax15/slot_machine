import os
import emoji
import random

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



def main():
    slots = Slot_Machine(100)
    while True:
        try:
            choice = int(input("Type amount to bet (1-5). "))
            slots.set_bet_and_spin(choice)

            if choice == 1:
                os.system('clear')
                r1, r2, r3 = slots.spin()              
                if r1 == r2 and r1 == r3:
                    slots.total += 5
                slots.make_board(r1, r2, r3)

        except ValueError:
            print("Please only enter 1.")


if __name__ == "__main__":
    main()