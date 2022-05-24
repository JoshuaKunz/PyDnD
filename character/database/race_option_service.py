from character.database.attribute_service import *

def get_race_options(character):
    output = ["human"]

    # get the attribute req for each race
    elf_req = get_elf_req()
    dwarf_req = get_dwarf_req()
    halfling_req = get_halfling_req()
    half_elf_req = get_halfelf_req()
    gnome_req = get_gnome_req()
    half_orc_req = get_halforc_req()

    # compare race req to character
    if character.dexterity >= elf_req['min_dex']:
        if character.constitution >= elf_req['min_con']:
            if character.intelligence >= elf_req['min_int']:
                if character.charisma >= elf_req['min_cha']:
                    output.append('elf')

  
    if character.constitution >= dwarf_req['min_con']:
        if character.strength >= dwarf_req['min_str']:
            output.append('dwarf')

    if character.dexterity >= halfling_req['min_dex']:
        if character.constitution >= halfling_req['min_con']:
            if character.intelligence >= halfling_req['min_int']:
                if character.strength >= halfling_req['min_str']:
                    output.append('halfling')

    if character.dexterity >= half_elf_req['min_dex']:
        if character.constitution >= half_elf_req['min_con']:
            if character.intelligence >= half_elf_req['min_int']:
                output.append('half_elf')

    if character.constitution >= gnome_req['min_con']:
        if character.intelligence >= gnome_req['min_int']:
            if character.strength >= gnome_req['min_str']:
                output.append('gnome')

    if character.strength >= half_orc_req['min_str']:
        if character.constitution >= half_orc_req['min_con']:
            output.append('half-orc')
    # if req is met then add the race to the output list
    return output
    # and finally...
    # after the list has been filled with the correct information, 
    # then return the results