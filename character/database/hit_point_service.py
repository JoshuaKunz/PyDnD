from utilities.dice import Dice

def get_hp_score(character):
    
    if character.cls == 'fighter' or character.cls == 'paladin' or character.cls == 'ranger':
        character.hp = Dice(10).roll(1)

    elif character.cls == 'mage' or character.cls == 'illusionist':
        character.hp = Dice(4).roll(1)
    
    elif character.cls == 'cleric' or character.cls == 'druid':
        character.hp = Dice(8).roll(1)
    
    elif character.cls == 'thief' or character.cls == 'bard':
        character.hp = Dice(6).roll(1)

    return character

def get_hp_adjust(character):
    
    char_con = character.constitution

    #and/or


    if character.cls == ('fighter' or character.cls == 'paladin' or character.cls == 'ranger') and char_con == 17:
        character.hp += 3

    elif character.cls == ('fighter' or character.cls == 'paladin' or character.cls == 'ranger') and char_con == 18:
        character.hp += 4

    elif character.cls == ('fighter' or character.cls == 'paladin' or character.cls == 'ranger') and char_con == 19:
        character.hp += 5
        
    elif char_con == 2 or char_con == 3:
        character.hp -= 2

    elif char_con >= 4 and char_con <= 6:
        character.hp -= 1

    elif char_con == 15:
        character.hp += 1

    elif char_con >= 16 and char_con <=19:
        character.hp += 2

    if character.hp < 4:
        character.hp =4

    return character


    