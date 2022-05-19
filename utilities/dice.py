import random

# create a function that takes the 
# number of dice and outputs a 
# random number based on the number of dice
# random number should be between 3 to 18
# store output in a variable, 6 outputs generated(str, ment, wis, dex, con, chr)
# account for attribute

class Dice: 
    def __init__(self, sides=6):
        self.sides = sides
        # DONE create a dice class that has a paramater to define how many
        # DONE sides is on the dice
    
    # returns the output of the dice roll
    def roll(self, count=1):
        return generate_random_number(count, self.sides * count)
        # DONE then create a method to roll the dice
        # DONE and output the random results

# paramaters must be integers
def generate_random_number(x, y):
    # x is the lowest possible number to output
    # y is the maximum number to output
    output = random.randint(x,y)

    return output