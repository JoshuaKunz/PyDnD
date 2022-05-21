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

       

    def __str__(self):
        return f"""Str: {self.strength}
Dex: {self.dexterity}
Con: {self.constitution}
Int: {self.intelligence}
Wis: {self.wisdom}
Cha: {self.charisma}"""