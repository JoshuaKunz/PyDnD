from utilities.dice import Dice


class Character:
    dice = Dice(6)

    def __init__(self):
        self.strength = self.dice.roll(3)
        self.dexterity = self.dice.roll(3)
        self.constitution = self.dice.roll(3)
        self.intelligence = self.dice.roll(3)
        self.wisdom = self.dice.roll(3)
        self.charisma = self.dice.roll(3)

        self.str_mod = Dice(100).roll(1)

        self.hp = 0
        self.thaco = 20

        self.race = None
        self.cls = None

        self.money = 0

        self.pp = 0
        self.ol = 0
        self.frt = 0
        self.hs = 0
        self.ms = 0
        self.dn = 0
        self.cw = 0
        self.rl = 0
        self.cp = 0

        # cha
        self.maximum_henchmen = 0
        self.loyalty_base = 0
        self.cha_reaction_adjustment = 0

        # con
        self.hp_adjustment = 0
        self.system_shock = 0
        self.ressurection_survival = 0
        self.poison_save = 0
        self.regeneration = 0

        # dex
        self.dex_reaction_adjustment = 0
        self.missile_attack_adjustment = 0
        self.defensive_adjustment = 0

        # int
        self.number_of_languages = 0
        self.max_spell_level = 0
        self.chance_learn_spell = 0
        self.max_number_of_spells = 0
        self.illusion_immunity = 0

        # str
        self.hit_probability = 0
        self.damage_adjust = 0
        self.weight_allowance = 0
        self.max_press = 0
        self.open_doors = 0
        self.bend_bars_lift_gates = 0

        # wis
        self.magic_defence_adjustment = 0
        self.bonus_spells = 0
        self.chance_spell_failure = 0
        self.spell_immunity = 0

        # saveings throw
        self.para_pois_dm = 0
        self.rod_staff_wand = 0
        self.petrify_poly = 0
        self.breath_weapon = 0
        self.spell = 0


    def __str__(self):
        string_builder = ''
        if self.cls == 'fighter' and self.strength == 18:
            string_builder += f"Str: {self.strength}/{self.str_mod}\n"
        else:
            string_builder += f"Str: {self.strength}\n"
        string_builder += f"""Dex: {self.dexterity}
Con: {self.constitution}
Int: {self.intelligence}
Wis: {self.wisdom}
Cha: {self.charisma}"""

        return string_builder

    def get_rogue_skills(self):

        string_builder = ""

        if self.cls == "thief":
            string_builder += f"""
pp: {self.pp} ms: {self.ms} cw: {self.cw}
ol: {self.ol} hs: {self.hs} rl: {self.rl}
frt: {self.frt} dn: {self.dn}"""

        elif self.cls == "bard":
            string_builder += f"""
pp: {self.pp} dn: {self.dn} cw: {self.cw}
rl: {self.rl} cp: {self.cp}"""
        return string_builder