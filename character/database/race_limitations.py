def race_class_limits(race,options):
# class_options needs to run first, then pass that list through here to get race qualified classes
    output = []

    fighter = ['human', 'elf', 'half-elf', 'halfling', 'dwarf', 'gnome', 'half-orc']
    paladin = ['human']
    ranger = ['human', 'elf', 'half-elf']
    mage = ['human', 'elf', 'half-elf']
    illusionist = ['human', 'gnome']
    cleric = ['human', 'elf', 'half-elf', 'halfling', 'dwarf', 'half-orc']
    druid = ['human', 'half-elf']
    thief = ['human', 'elf', 'half-elf', 'halfling', 'dwarf', 'gnome', 'half-orc']
    bard = ['human', 'half-elf']

    r = race
    a = output.append
    o = options

    if r in fighter and 'fighter' in o:
        a('fighter')
    if r in paladin and 'paladin' in o:
        a('paladin')
    if r in ranger and 'ranger' in o:
        a('ranger')
    if r in mage and 'mage' in o:
        a('mage')
    if r in illusionist and 'illusionist' in o:
        a('illusionist')
    if r in cleric and 'cleric' in o:
        a('cleric')
    if r in druid and 'druid' in o:
        a('druid')
    if r in thief and 'thief' in o:
        a('thief')
    if r in bard and 'bard' in o:
        a('bard')

    return output

