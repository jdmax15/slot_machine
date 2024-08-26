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
        
        result_1 = random.choice(emoji_dict)
        result_2 = random.choice(emoji_dict)
        result_3 = random.choice(emoji_dict)

        return result_1, result_2, result_3
    
# NEED TO FIX SPIN/BETTING LOGIC. IT CURRENTLY ONLY CHANGES MONEY IF YOU PRESS 1 AND KEEPS RESPINNING.
def main():
    slots = Slot_Machine(100)
    while True:
        try:
            choice = input("Type 1 to spin. ")
            slots.total -= 1

            if choice == "1":
                os.system('clear')
                r1, r2, r3 = slots.spin()              
                if r1 == r2 and r1 == r3:
                    slots.total += 5
                slots.make_board(r1, r2, r3)

        except ValueError:
            print("Please only enter 1.")


if __name__ == "__main__":
    main()