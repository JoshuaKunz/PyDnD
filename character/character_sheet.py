import json
import os
from utilities.string_utilities import write_positive as wp
from utilities.string_utilities import write_percent as wpc
from utilities.string_utilities import write_pounds as lbs
from utilities.string_utilities import nth

class CharacterSheet:

    class Type:
        json = 'json'
        txt = 'txt'
        sprdsht = 'spreadsheet'

    def display(character):
        pass

    def make_file(c, type=Type.txt):
        DOWNLOADS_DIR = f'C:\\Users\\{os.getlogin()}\\Downloads\\'
        
        if type == CharacterSheet.Type.json:
            file_name = 'character.json'
            jsonStr = json.dumps(c.__dict__)
            with open(DOWNLOADS_DIR + file_name, 'w') as f:
                f.write(jsonStr)
            return
        if type == CharacterSheet.Type.txt:
            file_name = 'character.txt'
            txtStr = f"""
Character:
Class: {c.cls} Race: {c.race} Level: ()
Alignment: () Gender: () Age: ()
HT: () WT: () Hair: () Eyes: ()
[{c.strength}] STR  |  %|HIT PROB: {wp(c.hit_probability)}|DMG ADJ: {wp(c.damage_adjust)}|WEIGHT ALLOW: {lbs(c.weight_allowance)}|MAX PRESS: {lbs(c.max_press)}|OPEN DOOR: {wp(c.open_doors)}|BEND BARS: {wpc(c.bend_bars_lift_gates)}|
[{c.dexterity}] DEX |REACTION ADJ: {wp(c.dex_reaction_adjustment)}|MISSILE ADJ: {wp(c.missile_attack_adjustment)}|DEFENCE ADJ: {wp(c.defensive_adjustment)}|
[{c.constitution}] CON |HIT POINT ADJ: {wp(c.hp_adjustment)}|SYSTEM SHOCK: {wpc(c.system_shock)}|RESURRECT SURVIVAL: {wpc(c.ressurection_survival)}|POISON SAVE: {wp(c.poison_save)}|REGENERATE: {wp(c.regeneration)}|
[{c.intelligence}] INT |MAX # OF LANG: {wp(c.number_of_languages)}|MAX SPELL LVL: {wp(c.max_spell_level)}|CHANCE TO LEARN: {wpc(c.chance_learn_spell)}|MAX SPELLS PER LEVEL: {wp(c.max_number_of_spells)}| ILLUSION IMMUNITY: {str(c.illusion_immunity)}|
[{c.wisdom}] WIS |MAGICAL DEF ADJ: {wp(c.magic_defence_adjustment)}|SPELL FAILURE: {wpc(c.chance_spell_failure)}|BONUS SPELLS: {nth(c.bonus_spells)}| SPELL IMMUNITY: {str(c.spell_immunity)}|
[{c.charisma}] CHA |MAX # HENCHMEN: {wp(c.maximum_henchmen)}|LOYALTY BASE: {wp(c.loyalty_base)}|REACTION ADJ: {wp(c.cha_reaction_adjustment)}|"""

            with open(DOWNLOADS_DIR + file_name, 'w') as f:
                f.write(txtStr)
            return