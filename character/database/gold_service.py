from utilities.dice import Dice

def get_money(character):

    war_cls = ['fighter', 'paladin', 'ranger']
    wiz_cls = ['mage', 'illusionist']
    prt_cls = ['cleric', 'druid']
    rge_cls = ['thief', 'bard']

    if character.cls in war_cls:
        character.money = Dice(4).roll(5) * 10

    if character.cls in wiz_cls:
        character.money = Dice(4).roll(2) * 10

    if character.cls in prt_cls:
        character.money = Dice(6).roll(3) * 10

    if character.cls in rge_cls:
        character.money = Dice(6).roll(2) *10

    return character