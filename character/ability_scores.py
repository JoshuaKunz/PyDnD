
def strength_ability_score(st):
    if st == 3:
        return Strength_Ability_Score_Obj(-3, -1, 5, 10, 2, 0)
    elif st == 4 or st == 5:
        return Strength_Ability_Score_Obj(-2, -1, 10, 25, 3, 0)
    elif st == 6 or st == 7:
        return Strength_Ability_Score_Obj(-1, 0, 20, 55, 4, 0)
    elif st == 8 or st == 9:
        return Strength_Ability_Score_Obj(0, 0, 35, 90, 5, 1)
    elif st == 10 or st == 11:
        return Strength_Ability_Score_Obj(0, 0, 40, 115, 6, 2)
    elif st == 12 or st == 13:
        return Strength_Ability_Score_Obj(0, 0, 45, 140, 7, 4)
    elif st == 14 or st == 15:
        return Strength_Ability_Score_Obj(0, 0, 55, 170, 8, 7)
    elif st == 16:
        return Strength_Ability_Score_Obj(0, +1, 70, 195, 9, 10)
    elif st == 17:
        return Strength_Ability_Score_Obj(+1, +1, 85, 220, 10, 13)
    elif st == 18:
        has_answered = False
        while(not has_answered):
            war = str(input("Will Character be Warrior Class 'Yes or No'")).lower()
            if war == "y" or war == "yes":
                has_answered = True
                pass
            elif war == "n" or war == "no":
                has_answered = True
                return Strength_Ability_Score_Obj(+1, +2, 110, 225, 11, 16)
            else:
                print("Please answer with a 'y/yes or n/no'")
                continue
            pass

class Strength_Ability_Score_Obj:
    def __init__(self,
                hit_probability,dmg_adjust,weight_allow,
                max_press,open_doors,lift_bend):

        self.hit_probabillity = hit_probability
        self.dmg_adjust = dmg_adjust
        self.weight_allow = weight_allow
        self.max_press = max_press
        self.open_doors = open_doors
        self.lift_bend = lift_bend


def dexterity_ability_score(dex):
    if dex == 3:
        return Dexterity_Ability_Score_Obj(-3, -3, +4)
    elif dex == 4:
        return Dexterity_Ability_Score_Obj(-2, -2, +3)
    elif dex == 5:
        return Dexterity_Ability_Score_Obj(-1, -1, +2)
    elif dex == 6:
        return Dexterity_Ability_Score_Obj(0, 0, +1)
    elif dex == 7:
        return Dexterity_Ability_Score_Obj(0, 0, 0)
    elif dex == 8:
        return Dexterity_Ability_Score_Obj(0, 0, 0)
    elif dex == 9:
        return Dexterity_Ability_Score_Obj(0, 0, 0)
    elif dex >= 10 and dex <= 14:
        return Dexterity_Ability_Score_Obj(0, 0, 0)
    elif dex == 15:
        return Dexterity_Ability_Score_Obj(0, 0, -1)
    elif dex == 16:
        return Dexterity_Ability_Score_Obj(+1, +1, -2)
    elif dex == 17:
        return Dexterity_Ability_Score_Obj(+2, +2, -3)
    elif dex == 18:
        return Dexterity_Ability_Score_Obj(+2, +2, -4)

class Dexterity_Ability_Score_Obj:
    def __init__(self,
                reaction_adj, missile_atk_adj, def_adj):
                
        self.reaction_adj = reaction_adj
        self.missile_atk_adj = missile_atk_adj
        self.def_adj = def_adj


def constitution_ability_score(con, char):
    if con == 3:
        return Constitution_Ability_Score_Obj(-2, 35, 40, 0, 0)
    elif con == 4:
        return Constitution_Ability_Score_Obj(-1, 40, 45, 0, 0)
    elif con == 5:
        return Constitution_Ability_Score_Obj(-1, 45, 50, 0, 0)
    elif con == 6:
        return Constitution_Ability_Score_Obj(-1, 50, 55, 0, 0)
    elif con == 7:
        return Constitution_Ability_Score_Obj(0, 55, 60, 0, 0)
    elif con == 8:
        return Constitution_Ability_Score_Obj(0, 60, 65, 0, 0)
    elif con == 9:
        return Constitution_Ability_Score_Obj(0, 65, 70, 0, 0)
    elif con == 10:
        return Constitution_Ability_Score_Obj(0, 70, 75, 0, 0)
    elif con == 11:
        return Constitution_Ability_Score_Obj(0, 75, 80, 0, 0)
    elif con == 12:
        return Constitution_Ability_Score_Obj(0, 80, 85, 0, 0)
    elif con == 13:
        return Constitution_Ability_Score_Obj(0, 85, 90, 0, 0)
    elif con == 14:
        return Constitution_Ability_Score_Obj(0, 88, 92, 0, 0)
    elif con == 15:
        return Constitution_Ability_Score_Obj(+1, 90, 94, 0, 0)
    elif con == 16:
        return Constitution_Ability_Score_Obj(+2, 95, 96, 0, 0)
    elif con == 17:
        if char.is_warrior:
            return Constitution_Ability_Score_Obj(+3, 97, 98, 0, 0)
        else:
            return Constitution_Ability_Score_Obj(+2, 97, 98, 0, 0)
    elif con == 18:
        if char.is_warrior:
            return Constitution_Ability_Score_Obj(+4, 99, 100, 0, 0)
        else:
            return Constitution_Ability_Score_Obj(+2, +4, 99, 100, 0, 0)

class Constitution_Ability_Score_Obj:
    def __init__(self,
                hp_adj, sys_shock, 
                res_survival, poison_save, regen):

        self.hp_adj = hp_adj
        self.sys_shock = sys_shock
        self.res_survival = res_survival
        self.poison_save = poison_save
        self.regen = regen


def intelligence_ability_score(int):
    if int == 3:
        return Intelligence_Ability_Score_Obj()
    elif int == 4:
        return Intelligence_Ability_Score_Obj()
    elif int == 5:
        return Intelligence_Ability_Score_Obj()
    elif int == 6:
        return Intelligence_Ability_Score_Obj()
    elif int == 7:
        return Intelligence_Ability_Score_Obj()
    elif int == 8:
        return Intelligence_Ability_Score_Obj()
    elif int == 9: 
        return Intelligence_Ability_Score_Obj()
    elif int == 10:
        return Intelligence_Ability_Score_Obj()
    elif int == 11:
        return Intelligence_Ability_Score_Obj()
    elif int == 12:
        return Intelligence_Ability_Score_Obj()
    elif int == 13:
        return Intelligence_Ability_Score_Obj()
    elif int == 14:
        return Intelligence_Ability_Score_Obj()
    elif int == 15:
        return Intelligence_Ability_Score_Obj()
    elif int == 16:
        return Intelligence_Ability_Score_Obj()
    elif int == 17:
        return Intelligence_Ability_Score_Obj()
    elif int == 18:
        return Intelligence_Ability_Score_Obj()
    else:
        pass
    
class Intelligence_Ability_Score_Obj:
    def __init__(self, 
                num_of_lang, max_spell_lvl, 
                chance_lrn_spell, max_num_spells, 
                illusion_immunity):
                
        self.num_of_lang = num_of_lang
        self.max_spell_lvl = max_spell_lvl
        self.chance_lrn_spell = chance_lrn_spell
        self.max_num_spells = max_num_spells
        self.illusion_immunity = illusion_immunity


def wisdom_ability_score(wis):
    if wis == 3:
        return Wisdom_Ability_Score_Obj()
    elif wis == 4:
        return Wisdom_Ability_Score_Obj()
    elif wis == 5:
        return Wisdom_Ability_Score_Obj()
    elif wis == 6:
        return Wisdom_Ability_Score_Obj()
    elif wis == 7:
        return Wisdom_Ability_Score_Obj()
    elif wis == 8:
        return Wisdom_Ability_Score_Obj()
    elif wis == 9:
        return Wisdom_Ability_Score_Obj()
    elif wis == 10:
        return Wisdom_Ability_Score_Obj()
    elif wis == 11:
        return Wisdom_Ability_Score_Obj()
    elif wis == 12:
        return Wisdom_Ability_Score_Obj()
    elif wis == 13:
        return Wisdom_Ability_Score_Obj()
    elif wis == 14:
        return Wisdom_Ability_Score_Obj()
    elif wis == 15:
        return Wisdom_Ability_Score_Obj()
    elif wis == 16:
        return Wisdom_Ability_Score_Obj()
    elif wis == 17:
        return Wisdom_Ability_Score_Obj()
    elif wis == 18:
        return Wisdom_Ability_Score_Obj()
    else:
        pass
    
class Wisdom_Ability_Score_Obj:
    def __init__(self, 
                magic_def_adj, bonus_spells, 
                chance_spell_failure, spell_immunity):

                
        self.magic_def_adj = magic_def_adj
        self.bonus_spells = bonus_spells
        self.chance_spell_failure = chance_spell_failure
        self.spell_imunity = spell_immunity


class Charisma_Ability_Score_Obj:
    def __init__(self, 
                max_henchmen, 
                loyalty_base, 
                react_adj):
        self.max_henchmen = max_henchmen
        self.loyalty_base = loyalty_base
        self.react_adj = react_adj