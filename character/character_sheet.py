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
        ul = file.ul
        li = file.li

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

        # race and class
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
        h4(cls="card-title", text="Hp: " + str(character.hp))
        div(close=True)
        div(close=True)

        #thac0 card
        div(cls="card")
        div(cls="card-body")
        h4(cls="card-title", text="THAC0: " + str(character.thaco)) #TODO: add thaco later
        div(close=True)
        div(close=True)
        #end race class on one line

        #end jumbotron
        div(close=True)

        # str table
        div(cls="container")
        div(cls="row")
        div(cls="mg-3 col-md-6")
        table(cls="table table-light")

        #table heads
        thead(cls="thead-light")
        th(cls="col-md-1", scope="col", text="STR: ")
        th(cls="text-center", scope="col", text="00%")
        th(cls="text-center", scope="col", text="Hit Prob")
        th(cls="text-center", scope="col", text="Damage Adj")
        th(cls="text-center", scope="col", text="Weight Allow")
        th(cls="text-center", scope="col", text="Max Press")
        th(cls="text-center", scope="col", text="Open Doors")
        th(cls="text-center", scope="col", text="Bend Bars")
        thead(close=True)
        #end table heads

        #table body
        tbody()
        #add rows

        #str row
        tr()

        th(cls="text-danger bg-warning", scope="row", header_font=True, text=character.strength)
        if character.strength == 18:
            td(cls="text-center bg-warning", text=str(character.strength) + "/" + str(character.str_mod) + "%")
        else:
            td(cls="text-center", text="N/A")

        td(cls="text-center", text=wp(character.hit_probability))
        td(cls="text-center", text=wp(character.damage_adjust))
        td(cls="text-center", text=lbs(character.weight_allowance))
        td(cls="text-center", text=lbs(character.max_press))
        td(cls="text-center", text=character.open_doors)
        td(cls="text-center", text=wpc(character.bend_bars_lift_gates))
        tr(close=True)
        #end str row

        tbody(close=True)
        table(close=True)
        #end str table

        #dex table
        table(cls="table table-light")
        #headers
        thead(cls="thead-light")
        th(cls="col-md-1", scope="col", text="DEX: ")
        th(cls="text-center", scope="col", text="Reaction Adj")
        th(cls="text-center", scope="col", text="Missile Adj")
        th(cls="text-center", scope="col", text="Defense Adj")
        #end headers
        thead(close=True)

        #body
        tbody()
        #rows
        th(cls="text-danger bg-warning", scope="row", header_font=True, text=character.dexterity)
        td(cls="text-center", text=wp(character.dex_reaction_adjustment))
        td(cls="text-center", text=wp(character.missile_attack_adjustment))
        td(cls="text-center", text=wp(character.defensive_adjustment))
        tbody(close=True)
        #end dex table
        table(close=True)

        #con table
        table(cls="table table-light")
        #table headers
        thead(cls="thead-light")
        th(cls="col-md-1", scope="col", text="CON: ")
        th(cls="text-center", scope="col", text="Hit Point Adj")
        th(cls="text-center", scope="col", text="System Shock")
        th(cls="text-center", scope="col", text="Resurrection Survival")
        th(cls="text-center", scope="col", text="Poison Save")
        th(cls="text-center", scope="col", text="Regenerate")
        thead(close=True)
        #end table headers
        #con table body
        tbody()
        #rows
        tr()
        th(cls="text-danger bg-warning", scope="row", header_font=True, text=character.constitution)
        td(cls="text-center", text=wp(character.hp_adjustment))
        td(cls="text-center", text=wpc(character.system_shock))
        td(cls="text-center", text=wpc(character.ressurection_survival))
        td(cls="text-center", text=wp(character.poison_save))
        td(cls="text-center", text=wp(character.regeneration))
        tr(close=True)
        tbody(close=True)
        #end con table body
        #end con table
        table(close=True)

        #int table
        table(cls="table table-light")
        #headers
        thead(cls="thead-light")
        th(cls="col-md-1", scope="col", text="INT: ")
        th(cls="text-center", scope="col", text="Max # of Lang")
        th(cls="text-center", scope="col", text="Max Spell Lvl")
        th(cls="text-center", scope="col", text="Chance to Learn")
        th(cls="text-center", scope="col", text="Max Spells/Lvl")
        th(cls="text-center", scope="col", text="Illusion Immunity")
        #end table headers
        thead(close=True)

        #table body
        tbody()
        #add rows
        tr()
        th(cls="text-danger bg-warning", scope="row", header_font=True, text=character.intelligence)
        td(cls="text-center", text=character.number_of_languages)
        td(cls="text-center", text=character.max_spell_level)
        td(cls="text-center", text=wpc(character.chance_learn_spell))
        td(cls="text-center", text=character.max_number_of_spells)
        td(cls="text-center", text=character.illusion_immunity)
        tr(close=True)
        #end table body

        table(close=True)
        #end int table

        #wis table
        table(cls="table table-light")
        #headers
        thead(cls="thead-light")
        th(cls="col-md-1", scope="col", text="WIS: ")
        th(cls="text-center", scope="col", text="Magical Def Adj")
        th(cls="text-center", scope="col", text="Spell Failure")
        th(cls="text-center", scope="col", text="Bonus Spells")
        th(cls="text-center", scope="col", text="Spell Immunity")
        thead(close=True)

        #wis table body
        tbody()
        #add rows
        tr()
        th(cls="text-danger bg-warning", scope="row", header_font=True, text=character.wisdom)
        td(cls="text-center", text=character.magic_defence_adjustment)
        td(cls="text-center", text=wpc(character.chance_spell_failure))
        td(cls="text-center", text=character.bonus_spells)
        td(cls="text-center", text=character.spell_immunity)
        tr(close=True)
        #end wis table body
        tbody(close=True)

        #end wis table
        table(close=True)

        #cha table
        table(cls="table table-light")
        #headers
        thead(cls="thead-light")
        th(cls="col-md-1", scope="col", text="CHA: ")
        th(cls="text-center", scope="col", text="Max # Henchmen")
        th(cls="text-center", scope="col", text="Loyalty Base")
        th(cls="text-center", scope="col", text="Reaction Adj")
        #endheaders
        thead(close=True)
        
        #cha body
        tbody()
        #add rows
        tr()
        th(cls="text-danger bg-warning", scope="row", header_font=True, text=character.charisma)
        td(cls="text-center", text=character.maximum_henchmen)
        td(cls="text-center", text=wp(character.loyalty_base))
        td(cls="text-center", text=wp(character.cha_reaction_adjustment))
        tr(close=True)
        #end body
        tbody(close=True)

        #end table
        table(close=True)

        div(close=True)
        #end div tables

        #column
        div(cls="col-md-6")

        #container
        div(cls="container h-100 d-flex flex-column")

        #row1
        div(cls="row h-25 flex-grow-1")
        div(cls="card")
        table(cls="table table-light")
        thead()
        th(scope="col", text="Weapon")
        th(scope="col", text="#AT")
        th(scope="col", text="Size")
        th(scope="col", text="Type")
        th(scope="col", text="Speed")
        th(scope="col", text="Damage")
        th(scope="col", text="Range/Special")
        thead(close=True)
        table(close=True)
        div(close=True)
        div(close=True)

        #row2
        div(cls="row h-75 flex-grow-1")
        div(cls="card")
        h4(cls="text-center card-title", text="Spells")
        div(close=True)
        div(close=True)

        #end container
        div(close=True)

        div(close=True)
        #end div row2

        div(close=True)

        #end container
        div(close=True)


        #div row
        div(cls="row")

        #theif skills div
        div(cls="col-md-2")
        div(cls="card")
        ul(cls="list-group list-group-light list-group-small")
        li(cls="list-group-item px-3", text="Pick Pockets: {}".format(wpc(character.pp)))
        li(cls="list-group-item px-3", text="Open Locks: {}".format(wpc(character.ol)))
        li(cls="list-group-item px-3", text="F/R Traps: {}".format(wpc(character.ol)))
        li(cls="list-group-item px-3", text="Move Silently: {}".format(wpc(character.ms)))
        li(cls="list-group-item px-3", text="Hide in Shadows: {}".format(wpc(character.hs)))
        li(cls="list-group-item px-3", text="Detect Noise: {}".format(wpc(character.dn)))
        li(cls="list-group-item px-3", text="Climb Walls: {}".format(wpc(character.cw)))
        li(cls="list-group-item px-3", text="Read Languages: {}".format(wpc(character.rl)))
        li(cls="list-group-item px-3", text="Backstab: X{}".format(2))
        ul(close=True)
        div(close=True)
        #end div thief skills
        div(close=True)

        div(cls="col-md-5")
        div(cls="card")
        h4(cls="text-center card-title", text="Inventory")
        div(close=True)
        div(close=True)


        #end row div
        div(close=True)


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