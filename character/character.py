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

        self.race = None
        self.cls = None

        self.pp = 0
        self.ol = 0
        self.frt = 0
        self.hs = 0
        self.ms = 0
        self.dn = 0
        self.cw = 0
        self.rl = 0

    def __str__(self):
        string_builder = f"""Str: {self.strength}
Dex: {self.dexterity}
Con: {self.constitution}
Int: {self.intelligence}
Wis: {self.wisdom}
Cha: {self.charisma}"""

        if self.cls == "thief":
            string_builder += f"""
pp: {self.pp} ms: {self.ms} cw: {self.cw}
ol: {self.ol} hs: {self.hs} rl: {self.rl}
frt: {self.frt} dn: {self.dn}"""

        return string_builder
