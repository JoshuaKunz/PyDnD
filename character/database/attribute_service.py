from character.database.models import *
from character.database.attribute_service import *


def get_str_value(abil_score):
    query = strength_ability_scores.select().where(strength_ability_scores.ability_score == abil_score)

    output = {}

    for row in query:
        output['ability_score'] = row.ability_score
        output['hit_probability'] = row.hit_probability
        output['damage_adjust'] = row.damage_adjust
        output['weight_allowance'] = row.weight_allowance
        output['max_press'] = row.max_press
        output['open_doors'] = row.open_doors
        output['bend_bars_lift_gates'] = row.bend_bars_lift_gates

    return output

def get_dex_value(abil_score):
    query = dexterity_ability_scores.select().where(dexterity_ability_scores.ability_score == abil_score)

    output = {}

    for row in query:
        output['ability_score'] = row.ability_score
        output['reaction_adjustment'] = row.reaction_adjustment
        output['missile_attack_adjustment'] = row.missile_attack_adjustment
        output['defensive_adjustment'] = row.defensive_adjustment

    return output

def get_con_value(abil_score):
    query = constitution_ability_scores.select().where(constitution_ability_scores.ability_score == abil_score)

    output = {}

    for row in query:
        output['ability_score'] = row.ability_score
        output['hp_adjustment'] = row.hp_adjustment
        output['system_shock'] = row.system_shock
        output['ressurection_survival'] = row.ressurection_survival
        output['poison_save'] = row.poison_save
        output['regeneration'] = row.regeneration

    return output

def get_int_value(abil_score):
    query = intelligence_ability_scores.select().where(intelligence_ability_scores.ability_score == abil_score)

    output = {}

    for row in query:
        output['ability_score'] = row.ability_score
        output['number_of_languages'] = row.number_of_languages
        output['max_spell_level'] = row.max_spell_level
        output['chance_learn_spell'] = row.chance_learn_spell
        output['max_number_of_spells'] = row.max_number_of_spells
        output['illusion_immunity'] = row.illusion_immunity

    return output

def get_wis_value(abil_score):
    query = wisdom_ability_scores.select().where(wisdom_ability_scores.ability_score == abil_score)

    output = {}

    for row in query:
        output['ability_score'] = row.ability_score
        output['magic_defence_adjustment'] = row.magic_defence_adjustment
        output['bonus_spells'] = row.bonus_spells
        output['chance_spell_failure'] = row.chance_spell_failure
        output['spell_immunity'] = row.spell_immunity

    return output

def get_cha_value(abil_score):
    query = charisma_ability_scores.select().where(charisma_ability_scores.ability_score == abil_score)

    output = {}

    for row in query:
        output['ability_score'] = row.ability_score
        output['maximum_henchmen'] = row.maximum_henchmen
        output['loyalty_base'] = row.loyalty_base
        output['reaction_adjustment'] = row.reaction_adjustment

    return output

def get_elf_req(): #get dex, con, int, cha
    query = race_ability_score_requirements.select().where(race_ability_score_requirements.race_name == "elf")

    output = {}

    for row in query:
        output['min_dex'] = row.min_dex
        output['min_con'] = row.min_con
        output['min_int'] = row.min_int
        output['min_cha'] = row.min_cha

    return output

def get_dwarf_req(): # get str, con
    query = race_ability_score_requirements.select().where(race_ability_score_requirements.race_name == "dwarf")

    output = {}

    for row in query:
        output['min_str'] = row.min_str
        output['min_con'] = row.min_con

    return output

def get_halfling_req(): # get dex, con, int
    query = race_ability_score_requirements.select().where(race_ability_score_requirements.race_name == "halfling")

    output = {}

    for row in query:
        output['min_dex'] = row.min_dex
        output['min_con'] = row.min_con
        output['min_int'] = row.min_int
        output['min_str'] = row.min_str

    return output

def get_halfelf_req(): # get dex, con, int
    query = race_ability_score_requirements.select().where(race_ability_score_requirements.race_name == "half-elf")

    output = {}

    for row in query:
        output['min_dex'] = row.min_dex
        output['min_con'] = row.min_con
        output['min_int'] = row.min_int

    return output

def get_gnome_req(): # get str, con ,int
    query = race_ability_score_requirements.select().where(race_ability_score_requirements.race_name == "gnome")
    
    output = {}

    for row in query:
        output['min_str'] = row.min_str
        output['min_con'] = row.min_con
        output['min_int'] = row.min_int

    return output


def get_fighter_req():# fighter get str
    query = subclass_ability_score_requirements.select().where(subclass_ability_score_requirements.subclass_name =="fighter")

    output = {}

    for row in query:
        output['min_str'] = row.min_str

    return output

def get_paladin_req():# paladin get str, con, wis, cha
    query = subclass_ability_score_requirements.select().where(subclass_ability_score_requirements.subclass_name =="paladin")

    output = {}

    for row in query:
        output['min_str'] = row.min_str
        output['min_con'] = row.min_con
        output['min_wis'] = row.min_wis
        output['min_cha'] = row.min_cha

    return output

def get_ranger_req():# ranger get str, con, wis, cha
    query = subclass_ability_score_requirements.select().where(subclass_ability_score_requirements.subclass_name =="ranger")

    output = {}

    for row in query:
        output['min_str'] = row.min_str
        output['min_con'] = row.min_con
        output['min_wis'] = row.min_wis
        output['min_dex'] = row.min_dex

    return output

def get_mage_req():# mage get str, con, wis, cha
    query = subclass_ability_score_requirements.select().where(subclass_ability_score_requirements.subclass_name =="mage")

    output = {}

    for row in query:
        output['min_int'] = row.min_int
       
    return output

def get_illusionist_req():# illusionist get dex
    query = subclass_ability_score_requirements.select().where(subclass_ability_score_requirements.subclass_name =="illusionist")

    output = {}

    for row in query:
        output['min_dex'] = row.min_dex

    return output

def get_cleric_req():# cleric get wisdom
    query = subclass_ability_score_requirements.select().where(subclass_ability_score_requirements.subclass_name =="cleric")

    output = {}

    for row in query:
        output['min_wis'] = row.min_wis

    return output

def get_druid_req():# druid get wis, cha
    query = subclass_ability_score_requirements.select().where(subclass_ability_score_requirements.subclass_name =="druid")

    output = {}

    for row in query:
        output['min_wis'] = row.min_wis
        output['min_cha'] = row.min_cha

    return output

def get_thief_req():# thief get dex
    query = subclass_ability_score_requirements.select().where(subclass_ability_score_requirements.subclass_name =="thief")

    output = {}

    for row in query:
        output['min_dex'] = row.min_dex

    return output

def get_bard_req():# bard get dex, int, cha
    query = subclass_ability_score_requirements.select().where(subclass_ability_score_requirements.subclass_name =="bard")

    output = {}

    for row in query:
        output['min_dex'] = row.min_dex
        output['min_int'] = row.min_int
        output['min_cha'] = row.min_cha

    return output