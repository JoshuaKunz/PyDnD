from utilities.dice import Dice
from character.character import Character
from utilities.string_utilities import write_positive
from character.database.race_option_service import *

print("Character Creator")
character = Character()

x = get_wis_value(10)
print(x)

# get the race options and store them in a variable
# racelist = get_race_options(character)

#iterate meaning for each
# for race in racelist:
    # print(race)

# loop through each of the race options
    # print each of them to the console

# print("H for Human \nD for Dwarf\nE for Elf\nG for Gnome\nS for Halfing\nP for HalfElf")

# has_answered = False
# while(not has_answered):
#     race_char = str(input("Choose Race for Character: ")).lower()
#     if race_char == "h":
#         has_answered = True
    

#     elif race_char == "d":
#         has_answered = True
    

#     elif race_char == "e":
#         has_answered = True
    

#     elif race_char == "g":
#         has_answered = True
  

#     elif race_char == "s":
#         has_answered = True
   

#     elif race_char =="p":
#         has_answered = True


# print("Choose the letter for the Class")
# print("F for Fighter \nP for Paladin \nR for Ranger \nM for Mage \nI for Illusionist \nC for Cleric \nD for Druid \nT for Thief \nB for Bard ")

# has_answered = False
# while(not has_answered):
#     prof = str(input("Choose Class for Character: ")).lower()
#     if prof == "f":
#         has_answered = True
    

#     elif prof == "p":
#         has_answered = True
    

#     elif prof == "r":
#         has_answered = True
    

#     elif prof == "m":
#         has_answered = True
  

#     elif prof == "i":
#         has_answered = True
   

#     elif prof =="c":
#         has_answered = True


#     elif prof =="d":
#         has_answered = True


#     elif prof =="t":
#         has_answered = True


#     elif prof =="b":
#         has_answered = True
