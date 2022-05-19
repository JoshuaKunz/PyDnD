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


class Human(Character):
    def __init__(self):
        super().__init__()

class Dwarf(Character):
    def __init__(self):
        super().__init__()
        self.constitution += 1
        self.charisma += 1

class Elf(Character):
    def __init__(self) -> None:
        super().__init__()
        self.dexterity += 1
        self.constitution -= 1

class HalfElf(Character):
    def __init__(self) -> None:
        super().__init__()

class Halfling(Character):
    def __init__(self) -> None:
        super().__init__()
        self.dex += 1
        self.strength -= 1