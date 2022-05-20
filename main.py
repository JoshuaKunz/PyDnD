from utilities.dice import Dice
from character.character import Character
from utilities.string_utilities import write_positive



print("Character Creator")
print("Choose the letter for the Race")
print("H for Human \nD for Dwarf\nE for Elf\nG for Gnome\nS for Halfing\nP for HalfElf")

has_answered = False
while(not has_answered):
    race = str(input("Choose Race for Character: ")).lower()
    if race == "h":
        has_answered = True
    

    elif race == "d":
        has_answered = True
    

    elif race == "e":
        has_answered = True
    

    elif race == "g":
        has_answered = True
  

    elif race == "s":
        has_answered = True
   

    elif race =="p":
        has_answered = True
    print(race)
    print(has_answered)

