from peewee import *
from .models import *

class DnDConnection:

    db = SqliteDatabase('dnd_info.db')

    def __init__(self) -> None:
        self.db.connect()
        self.db.create_tables([strength_ability_scores,
                                dexterity_ability_scores,
                                constitution_ability_scores,
                                intelligence_ability_scores,
                                wisdom_ability_scores,
                                charisma_ability_scores,
                                subclass_ability_score_requirements,
                                race_ability_score_requirements])
        self.db.close()

    def get_connection(self):
        return self.db
