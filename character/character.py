from utilities.dice import Dice

class Character:
    def __init__(self) -> None:
        dice = Dice()
        self.strength = dice.roll(3)
        self.intellegence = dice.roll(3)
        self.wisdom = dice.roll(3)
        self.dexterity = dice.roll(3)
        self.constitution = dice.roll(3)
        self.charisma = dice.roll(3)

        self.is_warrior = False
        self.is_rogue = False
        self.is_priest = False
        self.is_wizzard = False

        print(str(self))

    def __str__(self):
        return f"""strength={self.strength}
intellegence={self.intellegence}
wisdom={self.wisdom}\ndexterity={self.dexterity}
constitution={self.constitution}
charisma={self.charisma}"""
