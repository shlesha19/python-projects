
import random
def roll(sides=6):
    num_rolled = random.randint(1,sides)
    return num_rolled

def dice():
    sides = 6
    rolling = True
    while rolling:
        roll_again = input("Press ENTER = roll, Q = end")
        if roll_again.lower() != "q" :
            num_rolled = roll(sides)
            print("you rolled " , num_rolled)
        else:
                  rolling = False
    print("Thanks for Playing!!")

dice()