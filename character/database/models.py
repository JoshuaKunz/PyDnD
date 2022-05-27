from peewee import Model, SqliteDatabase, IntegerField, TextField

class BaseModel(Model):
    class Meta:
        database = SqliteDatabase('dnd_info.db')

class strength_ability_scores(BaseModel):
    ability_score = IntegerField(unique=True, null=False)
    hit_probability = IntegerField()
    damage_adjust = IntegerField()
    weight_allowance = IntegerField()
    max_press = IntegerField()
    open_doors = IntegerField()
    bend_bars_lift_gates = IntegerField()

class dexterity_ability_scores(BaseModel):
    ability_score = IntegerField(unique=True, null=False)
    reaction_adjustment = IntegerField()
    missile_attack_adjustment = IntegerField()
    defensive_adjustment = IntegerField()

class constitution_ability_scores(BaseModel):
    ability_score = IntegerField(unique=True, null=False)
    hp_adjustment = IntegerField()
    system_shock = IntegerField()
    ressurection_survival = IntegerField()
    poison_save = IntegerField()
    regeneration = IntegerField()

class intelligence_ability_scores(BaseModel):
    ability_score = IntegerField(unique=True, null=False)
    number_of_languages = IntegerField()
    max_spell_level = IntegerField()
    chance_learn_spell = IntegerField()
    max_number_of_spells = IntegerField()
    illusion_immunity = IntegerField()

class wisdom_ability_scores(BaseModel):
    ability_score = IntegerField(unique=True, null=False)
    magic_defence_adjustment = IntegerField()
    bonus_spells = IntegerField()
    chance_spell_failure = IntegerField()
    spell_immunity = TextField()

class charisma_ability_scores(BaseModel):
    ability_score = IntegerField(unique=True, null=False)
    maximum_henchmen = IntegerField()
    loyalty_base = IntegerField()
    reaction_adjustment = IntegerField()

class subclass_ability_score_requirements(BaseModel):
    subclass_name = TextField(unique=True, null=False)
    base_class_name = TextField(null=False)
    min_str = IntegerField()
    min_dex = IntegerField()
    min_con = IntegerField()
    min_int = IntegerField()
    min_wis = IntegerField()
    min_cha = IntegerField()

class race_ability_score_requirements(BaseModel):
    race_name = TextField(unique=True, null=False)
    min_str = IntegerField()
    min_dex = IntegerField()
    min_con = IntegerField()
    min_int = IntegerField()
    min_wis = IntegerField()
    min_cha = IntegerField()

class save_throw_values(BaseModel):
    class_group = TextField(unique=True, null=False)
    para_pois_dm = IntegerField()
    rod_staff_wand = IntegerField()
    petrify_poly = IntegerField()
    breath_weapon = IntegerField()
    spell = IntegerField()

