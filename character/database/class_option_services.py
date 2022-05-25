from character.database.attribute_service import *

def get_class_options(character):
    output = []

    # get the attribute req for each class
    fighter_req = get_fighter_req()
    paladin_req = get_paladin_req()
    ranger_req = get_ranger_req()
    mage_req = get_mage_req()
    illusionist_req = get_illusionist_req()
    cleric_req = get_cleric_req()
    druid_req = get_druid_req()
    thief_req = get_thief_req()
    bard_req = get_bard_req()


    # compare class req to character
    if character.strength >= fighter_req['min_str']:
        output.append('fighter')

  
    if character.constitution >= paladin_req['min_con']:
        if character.strength >= paladin_req['min_str']:
            if character.wisdom >= paladin_req['min_wis']:
                if character.charisma >= paladin_req['min_cha']:
                    output.append('paladin')

    if character.dexterity >= ranger_req['min_dex']:
        if character.constitution >= ranger_req['min_con']:
            if character.wisdom >= ranger_req['min_wis']:
                if character.strength >= ranger_req['min_str']:
                    output.append('ranger')
    
    if character.intelligence >= mage_req['min_int']:
        output.append('mage')

    if character.dexterity >= illusionist_req['min_dex']:
        output.append('illusionist')

    if character.wisdom >= cleric_req['min_wis']:
        output.append('cleric')

    if character.wisdom >= druid_req['min_wis']:
        if character.charisma >= druid_req['min_cha']:
            output.append('druid')

    if character.dexterity >= thief_req['min_dex']:
            output.append('thief')

    if character.dexterity >= bard_req['min_dex']:
        if character.intelligence >= bard_req['min_int']:
            if character.charisma >= bard_req['min_cha']:
                output.append('bard')
    # if req is met then add the race to the output list
    return output