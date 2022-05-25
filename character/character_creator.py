from character.character import Character
from character.database.race_option_service import *
from character.database.class_option_services import *
from character.database.racial_adjustment import get_racial_adjust
from utilities.colored_text import *
from character.database.thief_services import *
from character.character_sheet import CharacterSheet as cs

def character_creator():
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

    print("\nYou have chosen to be a(n) " + race + '\n')
    character.race = race

    character = get_racial_adjust(character)

    # add the attribute stats to the character
    character = set_all_attr_adjust(character)


    classlist = get_class_options(character)
    print("Which Class would you like to be?")
    for char_class in classlist:
        print(char_class)
    print()
    class_string =""
    for index in range(0, len(classlist)):
        class_string += str(index) +" for " + classlist[index] + "\n"

    print("Choose your class below.")

    print(class_string)

    has_answered = False
    while(not has_answered):
        user_input = int(input("What is your choice: "))

        if user_input > len(classlist) - 1:
            print("invalid class")
            continue
        else:
            has_answered = True
        char_class = classlist[user_input]
        
    character.cls = char_class
    print("\nYou have chosen to be a(n) " + char_class + '\n')
        # return char_class

    if character.cls == 'thief':
        character = get_all_thief_adjust(character)
    
    print_green(str(character))

    while True:
        answer = str(input("Would you like to save this to a file? y/n")).lower()

        if answer == 'y' or answer == 'yes':
            print("creating file in downloads folder.")
            cs.make_file(character, cs.Type.txt)
            break

        elif answer == 'n' or answer == 'no':
            print("No file will be created.")
            break
        else:
            print("Incorrect answer, try again.")
            continue
