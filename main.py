from utilities.dice import Dice
from character.character import Character
from utilities.string_utilities import write_positive
from character.database.race_option_service import *

print("Character Creator\n")
character = Character()
race = ""
char_class = ""

# get the race options and store them in a variable
racelist = get_race_options(character)
print("Available Characters:")
for race in racelist:
    print(race)
print()
race_string = ""
for index in range(0, len(racelist)):
    race_string += str(index) +" for " + racelist[index] + "\n"

print("Choose your race below.")

print(race_string)

has_answered = False
while(not has_answered):
    user_input = int(input("What is your choice: "))

    if user_input > len(racelist) - 1:
        print("nice try...")
        continue
    else:
        has_answered = True
    race = racelist[user_input]

print("You have chosen to be a(n) " + race)

print("Which Class would you like to be?")