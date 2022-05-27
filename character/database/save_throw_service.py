from character.database.models import save_throw_values

def get_save_throw(character):

    cls_grp = None

    war_grp = ['fighter', 'paladin', 'ranger']
    wiz_grp = ['mage', 'illusionist']
    prt_grp = ['cleric', 'druid']
    rge_grp = ['thief', 'bard']

    if character.cls in war_grp:
        cls_grp = 'warrior' 

    elif character.cls in wiz_grp:
        cls_grp = 'wizard'

    elif character.cls in prt_grp:
        cls_grp = 'priest'

    elif character.cls in rge_grp:
        cls_grp = 'rogue'

    query = save_throw_values.select().where(save_throw_values.class_group == cls_grp)

    output = {}

    for row in query:
        character.para_pois_dm = row.para_pois_dm
        character.rod_staff_wand = row.rod_staff_wand
        character.petrify_poly = row.petrify_poly
        character.breath_weapon = row.breath_weapon
        character.spell = row.spell


    # determine if char cls is dwarf, gnome, halfling or half-orc
    bonus_race = ['dwarf', 'gnome', 'halfling', 'half-orc']

    if character.race in bonus_race:
        if character.constitution >= 4 and character.constitution <= 6:
            character.para_pois_dm +=1
            character.rod_staff_wand +=1
            character.spell +=1
    
    if character.race in bonus_race:
        if character.constitution >= 7 and character.constitution <= 10:
            character.para_pois_dm += 2
            character.rod_staff_wand += 2
            character.spell +=2

    if character.race in bonus_race:
        if character.constitution >= 11 and character.constitution <= 13:
            character.para_pois_dm += 3
            character.rod_staff_wand += 3
            character.spell +=3

    if character.race in bonus_race:
        if character.constitution >= 14 and character.constitution <= 17:
            character.para_pois_dm += 4
            character.rod_staff_wand +=4
            character.spell += 4

    if character.race in bonus_race:
        if character.constitution == 18 or character.constitution == 19:
            character.para_pois_dm += 5
            character.rod_staff_wand += 5
            character.spell += 5

    return character


    # locate 3 base scores (r/s/w, poison, spell)
    # then compare with char con to determine the bonus
    # add the bonus to each individual value of base score
    # return to character the modified values 