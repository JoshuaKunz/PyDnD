from character.character import Character
from character.database.race_option_service import *
from character.database.class_option_services import *
from character.database.racial_adjustment import get_racial_adjust
from utilities.colored_text import *
from character.database.thief_services import *
from character.character_sheet import CharacterSheet as cs
from character.database.race_limitations import *
from character.database.hit_point_service import *
from character.database.thac0_service import *
from character.database.gold_service import get_money
from character.database.save_throw_service import get_save_throw
from utilities.colored_text import console

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

    print_green(str(character))

    options = get_class_options(character)
    classlist = race_class_limits(character.race, options)

    if classlist == []:
        print("There are no class options - program ending.")
        # kill the program
        return

# add print attributes here
    

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
    print("\nYou have chosen to be a(n) " + race + ' ' + char_class + '\n')
        

    if character.cls == 'thief':
        character = get_all_thief_adjust(character)

    if character.cls == 'bard':
        character = get_all_bard_adjust(character)

    sm = character.str_mod
    if character.cls == 'fighter' and character.strength == 18:
        if sm < 51:
            character.hit_probability = 1
            character.damage_adjust = 3
            character.weight_allowance = 135
            character.max_press = 280
            character.open_doors = 12
            character.bend_bars_lift_gates = 20

        if sm >= 51 and sm <= 75:
            character.hit_probability = 2
            character.damage_adjust = 3
            character.weight_allowance = 160
            character.max_press = 305
            character.open_doors = 13
            character.bend_bars_lift_gates = 25

        if sm >= 76 and sm <= 90:
            character.hit_probability = 2
            character.damage_adjust = 4
            character.weight_allowance = 185
            character.max_press = 330
            character.open_doors = 14
            character.bend_bars_lift_gates = 30

        if sm >= 91 and sm <= 99:
            character.hit_probability = 2
            character.damage_adjust = 5
            character.weight_allowance = 235
            character.max_press = 380
            character.open_doors = 15
            character.bend_bars_lift_gates = 35
        
        if sm == 100:
            character.hit_probability = 3
            character.damage_adjust = 6
            character.weight_allowance = 335
            character.max_press = 480
            character.open_doors = 16
            character.bend_bars_lift_gates = 40


    
    print_green(str(character))

    print()
    character = get_hp_score(character)
    character = get_hp_adjust(character)
    print_red('Hp: ' + str(character.hp))
    print()
    character = get_save_throw(character)
    print('p/p/dm:{}, r/s/w:{}, p/p:{}, brth:{}, spell:{}'.format(character.para_pois_dm, character.rod_staff_wand, character.petrify_poly, character.breath_weapon, character.spell))
    print()
    character = get_thac0(character)
    print_yellow('Thac0:' + str(character.thaco))
    print()
    character = get_money(character)
    print_blue('Coin:' + str(character.money))
    cs.create_gui(character)
    
    answer = str(input("Would you like to open the website for PDF converter?")).lower()

    if answer == "y" or answer == "yes":
        console.run_command("start https://www.sejda.com/html-to-pdf")

def __test_character_creator():

    character = Character()

    character.strength = 3
    character.dexterity = 3
    character.constitution = 3
    character.wisdom = 3
    character.charisma = 3
    character.intelligence = 3

    print("Test Character Creator\n")

    race = ""
    char_class = ""

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

    if classlist == []:
        print("There are no class options - program ending.")
        # kill the program
        return

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