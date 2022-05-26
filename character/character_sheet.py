import json
import os
from utilities.string_utilities import write_positive as wp
from utilities.string_utilities import write_percent as wpc
from utilities.string_utilities import write_pounds as lbs
from utilities.string_utilities import nth
from utilities.web import HTML as file

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

    def create_gui(character):
        div = file.div
        body = file.body
        p = file.p
        text = file.text
        h1 = file.h1
        h4 = file.h4
        table = file.table
        thead = file.thead
        tr = file.tr
        th = file.th
        td = file.td
        tbody = file.tbody

        file.start_html()

        body()
        
        #main div - container
        div(cls="container")

        #jumbotron
        div(cls="jumbotron text-center")
        h1()
        text("Character Sheet")
        h1(close=True)
        div(close=True)

        # race and class on one line
        div(cls="d-flex p-1 text-center")
        
        #cards
        #race card
        div(cls="card")
        div(cls="card-body")
        h4(cls="card-title", text="Race: " + character.race.title())
        div(close=True)
        div(close=True)

        #class card
        div(cls="card")
        div(cls="card-body")
        h4(cls="card-title", text="Class: " + character.cls.title())
        div(close=True)
        div(close=True)

        #hp card
        div(cls="card")
        div(cls="card-body")
        h4(cls="card-title", text="Hp: " + character.hp)
        div(close=True)
        div(close=True)

        #thac0 card
        div(cls="card")
        div(cls="card-body")
        h4(cls="card-title", text="THAC0: " + 20 - character.hit_probability) #TODO: add thaco later
        div(close=True)
        div(close=True)
        #end race class on one line

        #end jumbotron
        div(close=True)

        # str table
        div(cls="mg-3")
        table(cls="table table-light")

        #table heads
        thead(cls="thead-light")
        th(scope="col", text="STR: ")
        th(scope="col", text="Double Ott")
        th(scope="col", text="Hit Prob")
        th(scope="col", text="Damage Adj")
        th(scope="col", text="Weight Allow")
        th(scope="col", text="Max Press")
        th(scope="col", text="Open Doors")
        th(scope="col", text="Bend Bars")
        thead(close=True)
        #end table heads

        #table body
        tbody()
        #add rows

        #str row
        tr()

        th(cls="text-danger", scope="row", header_font=True, text=character.strength)
        if character.strength == 18:
            td(text=character.strength + "/" + character.str_mod + "%")
        else:
            td(text="N/A")

        td(text=wp(character.hit_probability))
        td(text=wp(character.damage_adjust))
        td(text=lbs(character.weight_allowance))
        td(text=lbs(character.max_press))
        td(text=character.open_doors)
        td(text=wpc(character.bend_bars_lift_gates))
        tr(close=True)
        #end str row

        tbody(close=True)
        table(close=True)
        #end str table

        #dex table
        table(cls="table table-light")
        #headers
        thead(cls="thead-light")
        th(scope="col", text="DEX: ")
        th(scope="col", text="Reaction Adj")
        th(scope="col", text="Missile Adj")
        th(scope="col", text="Defense Adj")
        #end headers
        thead(close=True)

        #body
        tbody()
        #rows
        th(cls="text-danger", scope="row", header_font=True, text=character.dexterity)
        td(text=wp(character.dex_reaction_adjustment))
        td(text=wp(character.missile_attack_adjustment))
        td(text=wp(character.defensive_adjustment))
        tbody(close=True)
        #end dex table
        table(close=True)

        #con table
        table(cls="table table-light")
        #table headers
        thead(cls="thead-light")
        th(scope="col", text="CON: ")
        th(scope="col", text="Hit Point Adj")
        th(scope="col", text="System Shock")
        th(scope="col", text="Resurrection Survival")
        th(scope="col", text="Poison Save")
        th(scope="col", text="Regenerate")
        thead(close=True)
        #end table headers
        #con table body
        tbody()
        #rows
        tr()
        th(cls="text-danger", scope="row", header_font=True, text=character.constitution)
        td(text=wp(character.hp_adjustment))
        td(text=wpc(character.system_shock))
        td(text=wpc(character.ressurection_survival))
        td(text=wp(character.poison_save))
        td(text=wp(character.regeneration))
        tr(close=True)
        tbody(close=True)
        #end con table body
        #end con table
        table(close=True)

        #int table
        table(cls="table table-light")
        #headers
        thead(cls="thead-light")
        th(scope="col", text="INT: ")
        th(scope="col", text="Max # of Lang")
        th(scope="col", text="Max Spell Lvl")
        th(scope="col", text="Chance to Learn")
        th(scope="col", text="Max Spells/Lvl")
        th(scope="col", text="Illusion Immunity")
        #end table headers
        thead(close=True)

        #table body
        tbody()
        #add rows
        tr()
        th(cls="text-danger", scope="row", header_font=True, text=character.intelligence)
        td(text=character.number_of_languages)
        td(text=character.max_spell_level)
        td(text=wpc(character.chance_learn_spell))
        td(text=character.max_number_of_spells)
        td(text=character.illusion_immunity)
        tr(close=True)
        #end table body

        table(close=True)
        #end int table

        #wis table
        table(cls="table table-light")
        #headers
        thead(cls="thead-light")
        th(scope="col", text="WIS: ")
        th(scope="col", text="Magical Def Adj")
        th(scope="col", text="Spell Failure")
        th(scope="col", text="Bonus Spells")
        th(scope="col", text="Spell Immunity")
        thead(close=True)

        #wis table body
        tbody()
        #add rows
        tr()
        th(cls="text-danger", scope="row", header_font=True, text=character.wisdom)
        td(text=character.magic_defence_adjustment)
        td(text=wpc(character.chance_spell_failure))
        td(text=character.bonus_spells)
        td(text=character.spell_immunity)
        tr(close=True)
        #end wis table body
        tbody(close=True)

        #end wis table
        table(close=True)

        #cha table
        table(cls="table table-light")
        #headers
        thead(cls="thead-light")
        th(scope="col", text="CHA: ")
        th(scope="col", text="Max # Henchmen")
        th(scope="col", text="Loyalty Base")
        th(scope="col", text="Reaction Adj")
        #endheaders
        thead(close=True)
        
        #cha body
        tbody()
        #add rows
        tr()
        th(cls="text-danger", scope="row", header_font=True, text=character.charisma)
        td(text=character.maximum_henchmen)
        td(text=wp(character.loyalty_base))
        td(text=wp(character.cha_reaction_adjustment))
        tr(close=True)
        #end body
        tbody(close=True)

        #end table
        table(close=True)

        div(close=True)
        #end div tables

        #end container
        div(close=True)
        body(close=True)
        file.end_html()
        CharacterSheet.create_gui_file()

    def create_gui_file():
        DOWNLOADS_DIR = f'C:\\Users\\{os.getlogin()}\\Downloads\\'
        file_name = 'character.html'
        with open(DOWNLOADS_DIR + file_name, 'w') as f:
            f.write(file.htmlStr)
        return