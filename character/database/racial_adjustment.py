
# get the attributes scores for character
def get_racial_adjust(character):
     
    if character.race == "dwarf":
        character.constitution = character.constitution + 1
        character.charisma = character.charisma - 1
        return character

    elif character.race == "elf":
        character.constitution = character.constitution - 1
        character.dexterity = character.dexterity +1
        return character

    elif character.race == "gnome":
        character.intelligence = character.intelligence + 1
        character.wisdom = character.wisdom - 1
        return character

    elif character.race == "halfling":
        character.dexterity = character.dexterity + 1
        character.strength = character.strength - 1
        return character

    else:
        return character


# get the race of choice
# determine the specific penalty_bonus for that race
