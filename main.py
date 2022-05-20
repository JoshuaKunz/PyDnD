from character.database.connections import DnDConnection
from character.database.strength_service import *
from utilities.dice import Dice
from utilities.string_utilities import *

dnd_db = DnDConnection()

dice = Dice(6)


for x in range(0,6):
    strdata = get_str_value(dice.roll(3))
    dexdata = get_dex_value(dice.roll(3))
    condata = get_con_value(dice.roll(3))
    intdata = get_int_value(dice.roll(3))
    wisdata = get_wis_value(dice.roll(3))
    chadata = get_cha_value(dice.roll(3))

    print(strdata)
    print(dexdata)
    print(condata)
    print(intdata)
    print(wisdata)
    print(chadata)