def get_thac0(character):

    if character.hit_probability <= 0:
        character.thaco += abs(character.hit_probability)
    
    else:
        character.thaco -= abs(character.hit_probability)

    return character