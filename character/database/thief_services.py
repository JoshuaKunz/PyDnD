
class thief_base_score:

    pp = 15
    ol = 10
    frt = 5
    ms = 10
    hs = 5
    dn = 15
    cw = 60
    rl = 0

def get_thief_base_score(character):

    character.pp = thief_base_score.pp
    character.ol = thief_base_score.ol
    character.frt = thief_base_score.frt
    character.ms = thief_base_score.ms
    character.hs = thief_base_score.hs
    character.dn = thief_base_score.dn
    character.cw = thief_base_score.cw
    character.rl = thief_base_score.rl
    return character

def get_thief_dex_adjust(character):

    if character.dexterity == 9:

        character.pp -= 15
        character.ol -= 10
        character.frt -= 10
        character.ms -= 20
        character.hs -= 10


    if character.dexterity == 10:

        character.pp -= 10
        character.ol -= 5
        character.frt -= 10
        character.ms -= 15
        character.hs -= 5

    if character.dexterity == 11:

        character.pp -= 5
        character.frt -= 5
        character.ms -= 10

    if character.race == 12:

        character.ms -= 5
        
    if character.race == 16:

        character.ol += 5

    if character.dexterity == 17:

        character.pp += 5
        character.ol += 10
        character.ms += 5
        character.hs += 5

    if character.dexterity == 18:

        character.pp += 10
        character.ol += 15
        character.frt += 5
        character.ms += 10
        character.hs += 10

    if character.dexterity == 19:
         
        character.pp += 15
        character.ol += 20
        character.frt += 10
        character.ms += 15
        character.hs += 15

    return character

def get_thief_race_adjust(character):

    if character.race == 'dwarf':

        character.ol += 10
        character.frt += 15
        character.cw -= 10
        character.rl -= 5

    if character.race == 'elf':

        character.pp += 5
        character.ol -= 5
        character.ms += 5
        character.hs += 10
        character.dn += 5

    if character.race == 'gnome':
        
        character.ol += 5
        character.frt += 10
        character.ms += 5
        character.hs += 5
        character.dn += 10
        character.cw -= 15

    if character.race == 'halfelf':

        character.pp += 10
        character.hs += 5

    if character.race == 'halfling':

        character.pp += 5
        character.ol += 5
        character.frt += 5
        character.ms += 10
        character.hs += 15
        character.dn += 5
        character.cw -= 15
        character.rl -= 5

    return character

def get_all_thief_adjust(character):

    character = get_thief_base_score(character)
    character = get_thief_dex_adjust(character)
    character = get_thief_race_adjust(character)
    return character