from character import Character

barbarianStats = [ 'str', 'con', 'dex', 'wis', 'int', 'cha']
bardStats = ['cha', 'dex', 'int', 'con', 'wis', 'str']
clericStats = ['wis', 'str', 'con', 'cha', 'int', 'dex']
druidStats = ['wis', 'int', 'str', 'dex', 'con', 'cha']
fighterStats = ['str', 'con', 'dex', 'wis', 'cha', 'int']
monkStats = ['dex', 'wis', 'con', 'str', 'int', 'cha']
paladinStats = ['wis', 'cha', 'str', 'con', 'int', 'dex']
rangerStats = ['dex', 'wis', 'int', 'con', 'cha', 'str']
rogueStats = ['dex', 'int', 'cha', 'wis', 'con', 'str']
sorcererStats = ['cha', 'int', 'wis', 'con', 'dex', 'str']
warlockStats = ['cha', 'con', 'dex', 'int', 'wis', 'str']
wizardStats = [ 'int', 'dex', 'con', 'cha', 'wis', 'str']

def create_character(name, charClass, race, rolls):
    # sort ze rolls
    rolls.sort(reverse=True)
    # make a character instance
    character = Character(name.title(), charClass.title(), race.title())

    if (charClass == 'barbarian'):
        statPriority = barbarianStats
    if (charClass == 'bard'):
        statPriority = bardStats
    if (charClass == 'cleric'):
        statPriority = clericStats
    if (charClass == 'druid'):
        statPriority = druidStats
    if (charClass == 'fighter'):
        statPriority = fighterStats
    if (charClass == 'monk'):
        statPriority = monkStats
    if (charClass == 'paladin'):
        statPriority = paladinStats
    if (charClass == 'ranger'):
        statPriority = rangerStats
    if (charClass == 'rogue'):
        statPriority = rogueStats
    if (charClass == 'sorcerer'):
        statPriority = sorcererStats
    if (charClass == 'warlock'):
        statPriority = warlockStats
    if (charClass == 'wizard'):
        statPriority = wizardStats
    
    # set the charcter's stats
    for x in statPriority:
        if x == 'str':
            character.str = rolls[0]
        if x == 'dex':
            character.dex = rolls[0]
        if x == 'con':
            character.con = rolls[0]
        if x == 'int':
            character.int = rolls[0]
        if x == 'wis':
            character.wis = rolls[0]
        if x == 'cha':
            character.cha = rolls[0]
        rolls.remove(rolls[0])
    
    # add stats for racial bonuses
    if race == 'human':
        character.str += 1
        character.dex += 1
        character.con += 1
        character.int += 1
        character.wis += 1
        character.cha += 1
    if race == 'hill dwarf':
        character.con += 2
        character.wis += 1
    if race == 'mountain dwarf':
        character.con += 2
        character.str += 2
    if race == 'dragonborn':
        character.str += 2
        character.cha += 1
    if race == 'drow elf':
        character.dex += 2
        character.cha += 1
    if race == 'high elf':
        character.dex += 2
        character.int += 1
    if race == 'wood elf':
        character.dex += 2
        character.wis += 1
    if race == 'forest gnome':
        character.int += 2
        character.dex += 1
    if race == 'rock gnome':
        character.int += 2
        character.con += 1
    if race == 'half-elf':
        character.cha += 2
        character.dex += 1
        character.str += 1
    if race == 'half-orc':
        character.str += 2
        character.con += 1
    if race == 'lightfoot halfling':
        character.dex += 2
        character.cha += 1
    if race == 'stout halfling':
        character.dex += 2
        character.con += 1
    if race == 'tiefling':
        character.cha += 2
        character.int += 1

    # return the character
    return character