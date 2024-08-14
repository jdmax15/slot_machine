import os
import sys
import random

class Slot_Machine:
    def __init__(self, total):
        self.total = total
        self.spin_result = self.spin()
        
        
    def make_board(self, r1, r2, r3):
        print(f"======================================")
        print(f"=========== SLOT MACHINE =============")
        print(f"======================================")
        print(f"======  {r1}  =====  {r2}  =====  {r3}  ======")
        print(f"======================================")
        print(f"======================================")
        print(f"======================================")


    def spin(self):
        result_1 = random.randint(1, 10)
        result_2 = random.randint(1, 10)
        result_3 = random.randint(1, 10)

        return result_1, result_2, result_3
    

def main():
    slots = Slot_Machine(100)
    print(f"Current money: {slots.total}")
    r1, r2, r3 = slots.spin_result
    slots.make_board(r1, r2, r3)


if __name__ == "__main__":
    main()