import os
import sys
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
        result_1 = random.randint(1, 2)
        result_2 = random.randint(1, 2)
        result_3 = random.randint(1, 2)

        return result_1, result_2, result_3
    
# NEED TO FIX SPIN/BETTING LOGIC. IT CURRENTLY ONLY CHANGES MONEY IF YOU PRESS 1 AND KEEPS RESPINNING.
def main():
    slots = Slot_Machine(100)
    while True:
        r1, r2, r3 = slots.spin()
        slots.make_board(r1, r2, r3)
        try:
            choice = input("Type 1 to spin.")
            slots.total -= 1
            if choice == "1" and r1 == r2 and r1 == r3:
                slots.total += 5

        except ValueError:
            print("Please only enter 1.")


if __name__ == "__main__":
    main()