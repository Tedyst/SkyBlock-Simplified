"""
pet_xp = [0, 100, 210, 330, 460, 605, 765, 940, 1130, 1340, 1570, 1820, 2095, 2395, 2725, 3085, 3485, 3925, 4415, 4955, 5555, 6215, 6945, 7745, 8625, 9585, 10635, 11785, 13045, 14425, 15935, 17585, 19385, 21345, 23475, 25785, 28285, 30985, 33905, 37065, 40485, 44185, 48185, 52535, 57285, 62485, 68185, 74485, 81485, 89285, 97985, 107685, 118485, 130485, 143785, 158485, 174685, 192485, 211985, 233285, 256485, 281685, 309085, 338885, 371285, 406485, 444685, 486085, 530885, 579285, 631485, 687685, 748085, 812885, 882285, 956485, 1035685, 1120385, 1211085, 1308285, 1412485, 1524185, 1643885, 1772085, 1909285, 2055985, 2212685, 2380385, 2560085, 2752785, 2959485, 3181185, 3418885, 3673585, 3946285, 4237985, 4549685, 4883385, 5241085, 5624785, 6036485, 6478185, 6954885, 7471585, 8033285, 8644985, 9311685, 10038385, 10830085, 11691785, 12628485, 13645185, 14746885, 15938585, 17225285, 18611985, 20108685, 21725385, 23472085, 25358785]

def xp_slice(start):
	diff = pet_xp[start - 1]
	return [xp - diff for xp in pet_xp[start-1:start+99]]

pet_xp = {'common': xp_slice(1), 'uncommon': xp_slice(7), 'rare': xp_slice(12), 'epic': xp_slice(17), 'legendary': xp_slice(21)}
"""

PET_RARITIES = ['common', 'uncommon', 'rare', 'epic', 'legendary']

PET_XP = {
    'common': [0, 100, 210, 330, 460, 605, 765, 940, 1130, 1340, 1570, 1820, 2095, 2395, 2725, 3085, 3485, 3925, 4415,
               4955, 5555, 6215, 6945, 7745, 8625, 9585, 10635, 11785, 13045, 14425, 15935, 17585, 19385, 21345, 23475,
               25785, 28285, 30985, 33905, 37065, 40485, 44185, 48185, 52535, 57285, 62485, 68185, 74485, 81485, 89285,
               97985, 107685, 118485, 130485, 143785, 158485, 174685, 192485, 211985, 233285, 256485, 281685, 309085,
               338885, 371285, 406485, 444685, 486085, 530885, 579285, 631485, 687685, 748085, 812885, 882285, 956485,
               1035685, 1120385, 1211085, 1308285, 1412485, 1524185, 1643885, 1772085, 1909285, 2055985, 2212685,
               2380385, 2560085, 2752785, 2959485, 3181185, 3418885, 3673585, 3946285, 4237985, 4549685, 4883385,
               5241085, 5624785],
    'uncommon': [0, 175, 365, 575, 805, 1055, 1330, 1630, 1960, 2320, 2720, 3160, 3650, 4190, 4790, 5450, 6180, 6980,
                 7860, 8820, 9870, 11020, 12280, 13660, 15170, 16820, 18620, 20580, 22710, 25020, 27520, 30220, 33140,
                 36300, 39720, 43420, 47420, 51770, 56520, 61720, 67420, 73720, 80720, 88520, 97220, 106920, 117720,
                 129720, 143020, 157720, 173920, 191720, 211220, 232520, 255720, 280920, 308320, 338120, 370520, 405720,
                 443920, 485320, 530120, 578520, 630720, 686920, 747320, 812120, 881520, 955720, 1034920, 1119620,
                 1210320, 1307520, 1411720, 1523420, 1643120, 1771320, 1908520, 2055220, 2211920, 2379620, 2559320,
                 2752020, 2958720, 3180420, 3418120, 3672820, 3945520, 4237220, 4548920, 4882620, 5240320, 5624020,
                 6035720, 6477420, 6954120, 7470820, 8032520, 8644220],
    'rare': [0, 275, 575, 905, 1265, 1665, 2105, 2595, 3135, 3735, 4395, 5125, 5925, 6805, 7765, 8815, 9965, 11225,
             12605, 14115, 15765, 17565, 19525, 21655, 23965, 26465, 29165, 32085, 35245, 38665, 42365, 46365, 50715,
             55465, 60665, 66365, 72665, 79665, 87465, 96165, 105865, 116665, 128665, 141965, 156665, 172865, 190665,
             210165, 231465, 254665, 279865, 307265, 337065, 369465, 404665, 442865, 484265, 529065, 577465, 629665,
             685865, 746265, 811065, 880465, 954665, 1033865, 1118565, 1209265, 1306465, 1410665, 1522365, 1642065,
             1770265, 1907465, 2054165, 2210865, 2378565, 2558265, 2750965, 2957665, 3179365, 3417065, 3671765, 3944465,
             4236165, 4547865, 4881565, 5239265, 5622965, 6034665, 6476365, 6953065, 7469765, 8031465, 8643165, 9309865,
             10036565, 10828265, 11689965, 12626665],
    'epic': [0, 440, 930, 1470, 2070, 2730, 3460, 4260, 5140, 6100, 7150, 8300, 9560, 10940, 12450, 14100, 15900, 17860,
             19990, 22300, 24800, 27500, 30420, 33580, 37000, 40700, 44700, 49050, 53800, 59000, 64700, 71000, 78000,
             85800, 94500, 104200, 115000, 127000, 140300, 155000, 171200, 189000, 208500, 229800, 253000, 278200,
             305600, 335400, 367800, 403000, 441200, 482600, 527400, 575800, 628000, 684200, 744600, 809400, 878800,
             953000, 1032200, 1116900, 1207600, 1304800, 1409000, 1520700, 1640400, 1768600, 1905800, 2052500, 2209200,
             2376900, 2556600, 2749300, 2956000, 3177700, 3415400, 3670100, 3942800, 4234500, 4546200, 4879900, 5237600,
             5621300, 6033000, 6474700, 6951400, 7468100, 8029800, 8641500, 9308200, 10034900, 10826600, 11688300,
             12625000, 13641700, 14743400, 15935100, 17221800, 18608500],
    'legendary': [0, 660, 1390, 2190, 3070, 4030, 5080, 6230, 7490, 8870, 10380, 12030, 13830, 15790, 17920, 20230,
                  22730, 25430, 28350, 31510, 34930, 38630, 42630, 46980, 51730, 56930, 62630, 68930, 75930, 83730,
                  92430, 102130, 112930, 124930, 138230, 152930, 169130, 186930, 206430, 227730, 250930, 276130, 303530,
                  333330, 365730, 400930, 439130, 480530, 525330, 573730, 625930, 682130, 742530, 807330, 876730,
                  950930, 1030130, 1114830, 1205530, 1302730, 1406930, 1518630, 1638330, 1766530, 1903730, 2050430,
                  2207130, 2374830, 2554530, 2747230, 2953930, 3175630, 3413330, 3668030, 3940730, 4232430, 4544130,
                  4877830, 5235530, 5619230, 6030930, 6472630, 6949330, 7466030, 8027730, 8639430, 9306130, 10032830,
                  10824530, 11686230, 12622930, 13639630, 14741330, 15933030, 17219730, 18606430, 20103130, 21719830,
                  23466530, 25353230]
}


def _pigman(profile, *, dungeon=False):
    # Buffs the Pigman sword by (Pet lvl * 0.4) damage and (Pet lvl * 0.25) strength. (All)
    # Deal (Pet lvl * 0.2%) extra damage to monsters level 100 and up. (Legendary)
    if profile.weapon == 'PIGMAN_SWORD':
        profile.weapon.stats.add_stat('damage', profile.pet.level * 0.4)
        profile.weapon.stats.add_stat('strength', profile.pet.level * 0.25)


def _elephant(profile, *, dungeon=False):  # (tbd)
    if profile.pet.rarity in ('common', 'uncommon', 'rare'):
        profile.stats.add_modifier('health', lambda stat: stat + (profile.pet.level / 10) * (
                profile.stats.get_stat('speed', dungeon=dungeon) // 100))
    else:
        profile.stats.add_modifier('health', lambda stat: stat + (profile.pet.level / 5) * (
                profile.stats.get_stat('speed', dungeon=dungeon) // 100))
    if profile.pet.rarity not in ('common', 'uncommon'):
        profile.stats.add_modifier('health', lambda stat: stat + (profile.pet.level / 100) * (
                profile.stats.get_stat('defense', dungeon=dungeon) // 10))


def _hound(profile, *, dungeon=False):
    if profile.pet.rarity == 'legendary':
        profile.stats.add_stat('attack speed', profile.pet.level * 0.1)


def _enderdragon(profile, *, dungeon=False):
    # Deal (Pet lvl * 0.25%) more damage to end mobs. (All)
    # Buffs the Aspect of the Dragon sword by (Pet lvl * 0.5) damage and (Pet lvl * 0.3) strength. (All)
    # Increases all stats by (Pet lvl * 0.1%). (Legendary)
    if profile.weapon == 'ASPECT_OF_THE_DRAGON':
        profile.weapon.stats.add_stat('damage', profile.pet.level * 0.5)
        profile.weapon.stats.add_stat('strength', profile.pet.level * 0.3)
    if profile.pet.rarity == 'legendary':
        profile.stats.multiplier += profile.pet.level * 0.001


def _bee(profile, *, dungeon=False):
    # Gain (1 + (Pet lvl * 0.02)) Intelligence and (1 + (Pet lvl * 0.02)) Strength for each nearby bee. (Max 15) (Common)
    # (1+ (Pet lvl * 0.09) INT and (1 + (Pet lvl * 0.07)) STR on Rare)
    # (1+ (Pet lvl * 0.14) INT and (1 + (Pet lvl * 0.11)) STR on Epic)
    # (1+ (Pet lvl * 0.19) INT and (1 + (Pet lvl * 0.14)) STR on Legendary)
    profile.stats.add_stat('intelligence', 1 + profile.pet.level *
                           {'common': 0.02, 'uncommon': 0.02, 'rare': 0.09, 'epic': 0.14, 'legendary': 0.19}[
                               profile.pet.rarity])
    profile.stats.add_stat('strength', 1 + profile.pet.level *
                           {'common': 0.02, 'uncommon': 0.02, 'rare': 0.07, 'epic': 0.11, 'legendary': 0.14}[
                               profile.pet.rarity])


def _squid(profile, *, dungeon=False):
    # Buffs the Ink Wand by (Pet lvl * 0.3) damage and (Pet lvl * 0.1) strength. (Rare) (0.4 DMG and 0.2 STR on Epic, Legendary)
    if profile.pet.rarity not in ('common', 'uncommon') and profile.weapon == 'INK_WAND':
        profile.weapon.stats.add_stat('damage', profile.pet.level * {'rare': 0.3, 'epic': 0.4, 'legendary': 0.4}[
            profile.pet.rarity])
        profile.weapon.stats.add_stat('strength', profile.pet.level * {'rare': 0.1, 'epic': 0.2, 'legendary': 0.2}[
            profile.pet.rarity])


def _parrot(profile, *, dungeon=False):
    # Gives (5 + (Pet lvl * 0.25)) strength to profiles within 20 Blocks (No stack). (Legendary)
    if profile.pet.rarity == 'legendary':
        profile.stats.add_stat('strength', 5 + (profile.pet.level * 0.25))


def _blaze(profile, *, dungeon=False):
    # Upgrades Blaze Armor stats and ability by (Pet lvl * 0.4%). (All)
    # Double effects of Hot Potato Books. (Legendary)
    if profile.armor == {'helmet': 'BLAZE_HELMET', 'chestplate': 'BLAZE_CHESTPLATE', 'leggings': 'BLAZE_LEGGINGS',
                         'boots': 'BLAZE_BOOTS'} \
            or profile.armor == {'helmet': 'FROZEN_BLAZE_HELMET', 'chestplate': 'FROZEN_BLAZE_CHESTPLATE',
                                 'leggings': 'FROZEN_BLAZE_LEGGINGS', 'boots': 'FROZEN_BLAZE_BOOTS'}:
        for piece in profile.armor.values():
            if piece:
                piece.stats.multiplier += profile.pet.level * 0.004
    if profile.pet.rarity == 'legendary':
        for piece in profile.armor.values():
            if piece:
                piece.stats.add_stat('health', piece.hot_potatos * 4)
                piece.stats.add_stat('defense', piece.hot_potatos * 2)
        if profile.weapon:
            profile.weapon.stats.add_stat('damage', profile.weapon.hot_potatos * 2)
            profile.weapon.stats.add_stat('strength', profile.weapon.hot_potatos * 2)


def _blackcat(profile, *, dungeon=False):  # (tbd)
    profile.stats.add_stat('speed', profile.pet.level)
    profile.stats.add_stat('speed cap', profile.pet.level)
    profile.stats.add_modifier('pet luck', lambda stat: stat * 1.15)
    profile.stats.add_modifier('magic find', lambda stat: stat * 1.15)


def _flyingfish(profile, *, dungeon=False):
    # Gives (Pet lvl * 0.4) strength when near water. (Rare) (0.5 on Epic, Legendary)
    # Increases the stats of Diver's Armor by (Pet lvl * 0.3%). (Legendary)
    if profile.pet.rarity == 'legendary' and profile.armor == {'helmet': 'DIVER_HELMET',
                                                               'chestplate': 'DIVER_CHESTPLATE',
                                                               'leggings': 'DIVER_LEGGINGS', 'boots': 'DIVER_BOOTS'}:
        for piece in profile.armor.values():
            piece.stats.multiplier += profile.pet.level * 0.003


def _magmacube(profile, *, dungeon=False):
    # Deal (Pet lvl * 0.25%) more damage to slimes. (Rare, Epic, Legendary)
    # Buffs the stats of Ember Armor by (Pet lvl * 1%). (Legendary)
    if profile.pet.rarity == 'legendary' and profile.armor == {'helmet': 'BLAZE_HELMET',
                                                               'chestplate': 'BLAZE_CHESTPLATE',
                                                               'leggings': 'BLAZE_LEGGINGS', 'boots': 'BLAZE_BOOTS'}:
        for piece in profile.armor.values():
            piece.stats.multiplier += profile.pet.level * 0.01


def _jerry(profile, *, dungeon=False):
    if profile.pet.rarity == 'legendary' and profile.weapon == 'ASPECT_OF_THE_JERRY':
        profile.weapon.stats.add_stat('damage', profile.pet.level * 0.1)


def _silverfish(profile, *, dungeon=False):  # (tbd)
    profile.stats.add_stat('true defense', profile.pet.level *
                           {'common': 0.05, 'uncommon': 0.1, 'rare': 0.1, 'epic': 0.15, 'legendary': 0.15}[
                               profile.pet.rarity])


def _turtle(profile, *, dungeon=False):  # (tbd)
    profile.stats.add_modifier('defense', lambda stat: stat * (3 + profile.pet.level * 0.17))


def _zombie(profile, *, dungeon=False):  # (tbd)
    for piece in profile.armor.values():
        if piece.internal_name.startswith('REVENANT_') or piece.internal_name.startswith('ZOMBIE_'):
            piece.stats.add_modifier('defense', lambda stat: stat * profile.pet.level / 4)


def _dolphin(profile, *, dungeon=False):  # (tbd)
    if profile.pet.rarity in ('rare', 'epic', 'legendary'):
        profile.stats.add_modifier('sea creature chance', lambda stat: stat * (1 + profile.pet.level / 1000))


def _lion(profile, *, dungeon=False):
    # Adds (Pet lvl * 0.03) damage to your weapons. (Common) (0.05 on Uncommon) (0.1 on Rare) (0.15 on Epic) (0.2 on Legendary)
    # Increases damage dealt by (Pet lvl * 0.3%) on your first hit on a mob. (Rare) (0.4% on Epic) (0.5% on Legendary)
    # Deal (Pet lvl * 0.3%) weapon damage against mobs below level 80. (Legendary)
    if profile.weapon:
        profile.weapon.stats.add_stat('damage', profile.pet.level *
                                      {'common': 0.03, 'uncommon': 0.05, 'rare': 0.1, 'epic': 0.15,
                                       'legendary': 0.2}[profile.pet.rarity])


def _yeti(profile, *, dungeon=False):
    profile.stats.add_modifier('defense', lambda stat: stat + profile.stats.get_stat('strength', dungeon=dungeon) / 100)
    if profile.pet.rarity == 'legendary' and profile.weapon == 'YETI_SWORD':
        profile.weapon.stats.add_stat('damage', 100)
        profile.weapon.stats.add_stat('intelligence', 100)


def _bluewhale(profile, *, dungeon=False):  # (tbd)
    if profile.pet.rarity == 'legendary':
        profile.stats.add_modifier('health', lambda stat: stat * (1 + profile.pet.level / 500))
    if profile.pet.rarity in ('rare', 'epic', 'legendary'):
        profile.stats.add_modifier('defense', lambda stat: stat + (profile.pet.level * 0.03) * (
                profile.stats.get_stat('defense', dungeon=dungeon) // 20))


PETS = {
    # Template
    'PET': {
        'name': 'Pet',
        'stats': {},
        'ability': None,
        'type': 'combat',
    },
    'SKELETON_HORSE': {
        'name': 'Skeleton Horse',
        'stats': {
            'intelligence': lambda lvl: lvl,
            'speed': lambda lvl: lvl / 2
        },
        'ability': None,
        'type': 'combat',
    },
    'SNOWMAN': {
        'name': 'Snowman',
        'stats': {
            'damage': lambda lvl: lvl / 4,
            'strength': lambda lvl: lvl / 4,
            'crit damage': lambda lvl: lvl / 4
        },
        'ability': None,
        'type': 'combat',
    },
    'BAT': {
        'name': 'Bat',
        'stats': {
            'intelligence': lambda lvl: lvl,
            'speed': lambda lvl: lvl / 20
        },
        'ability': None,
        'type': 'mining',
    },
    'SHEEP': {
        'name': 'Sheep',
        'stats': {
            'intelligence': lambda lvl: lvl,
            'ability damage': lambda lvl: lvl / 2,
        },
        # Increases your total  Mana by (Pet lvl * 0.25%) while in dungeons. (Legendary)
        'ability': None,
        'type': 'alchemy',
    },
    'CHICKEN': {
        'name': 'Chicken',
        'stats': {
            'health': lambda lvl: lvl * 2
        },
        'ability': None,
        'type': 'farming',
    },
    'WITHER_SKELETON': {
        'name': 'Wither Skeleton',
        'stats': {
            'strength': lambda lvl: lvl / 4,
            'crit chance': lambda lvl: lvl / 20,
            'crit damage': lambda lvl: lvl / 4,
            'defense': lambda lvl: lvl / 4,
            'intelligence': lambda lvl: lvl / 4
        },
        # Deal (Pet lvl * 0.5%) more damage against wither mobs. (All)
        # Upon hitting an enemy inflict the wither effect for (Pet lvl * 2%) damage over 3 seconds (No stack). (Legendary)
        'ability': None,
        'type': 'combat',
    },
    'SILVERFISH': {
        'name': 'Silverfish',
        'stats': {
            'defense': lambda lvl: lvl,
            'health': lambda lvl: lvl / 5,
        },
        'ability': _silverfish,
        'type': 'mining',
    },
    'RABBIT': {
        'name': 'Rabbit',
        'stats': {
            'health': lambda lvl: lvl,
            'speed': lambda lvl: lvl / 5
        },
        'ability': None,
        'type': 'farming',
    },
    'HORSE': {
        'name': 'Horse',
        'stats': {
            'intelligence': lambda lvl: lvl / 2,
            'speed': lambda lvl: lvl / 4
        },
        # While riding your horse, gain (Pet lvl * 0.25%) bow damage. (Legendary)
        'ability': None,
        'type': 'combat',
    },
    'PIGMAN': {
        'name': 'Pigman',
        'stats': {
            'strength': lambda lvl: lvl / 2,
            'defense': lambda lvl: lvl / 2
        },
        # Buffs the Pigman sword by (Pet lvl * 0.4) damage and (Pet lvl * 0.25) strength. (All)
        # Deal (Pet lvl * 0.2%) extra damage to monsters level 100 and up. (Legendary)
        'ability': _pigman,
        'type': 'combat',
    },
    'WOLF': {
        'name': 'Wolf',
        'stats': {
            'crit damage': lambda lvl: lvl / 10,
            'true defense': lambda lvl: lvl / 10,
            'speed': lambda lvl: lvl / 5,
            'health': lambda lvl: lvl / 2
        },
        # Gain (Pet lvl * 0.1%) crit damage for every nearby wolf (max 10). (Rare) (0.15% for Epic, Legendary)
        'ability': None,
        'type': 'combat',
    },
    'OCELOT': {
        'name': 'Ocelot',
        'stats': {
            'speed': lambda lvl: lvl / 2
        },
        'ability': None,
        'type': 'foraging',
    },
    'LION': {
        'name': 'Lion',
        'stats': {
            'strength': lambda lvl: lvl / 2,
            'speed': lambda lvl: lvl / 4
        },
        # Adds (Pet lvl * 0.03) damage to your weapons. (Common) (0.05 on Uncommon) (0.1 on Rare) (0.15 on Epic) (0.2 on Legendary)
        # Increases damage dealt by (Pet lvl * 0.3%) on your first hit on a mob. (Rare) (0.4% on Epic) (0.5% on Legendary)
        # Deal (Pet lvl * 0.3%) weapon damage against mobs below level 80. (Legendary)
        'ability': _lion,
        'type': 'foraging',
    },
    'ENDER_DRAGON': {
        'name': 'Dragon',
        'stats': {
            'strength': lambda lvl: lvl / 2,
            'crit chance': lambda lvl: lvl / 10,
            'crit damage': lambda lvl: lvl / 2
        },
        # Deal (Pet lvl * 0.25%) more damage to end mobs. (All)
        # Buffs the Aspect of the Dragon sword by (Pet lvl * 0.5) damage and (Pet lvl * 0.3) strength. (All)
        # Increases all stats by (Pet lvl * 0.1%). (Legendary)
        'ability': _enderdragon,
        'type': 'combat',
    },
    'GUARDIAN': {
        'name': 'Guardian',
        'stats': {
            'intelligence': lambda lvl: lvl,
            'defense': lambda lvl: lvl / 2
        },
        'ability': None,
        'type': 'fishing',
    },
    'ENDERMAN': {
        'name': 'Enderman',
        'stats': {
            'crit damage': lambda lvl: lvl * 0.75
        },
        'ability': None,
        'type': 'combat',
    },
    'BLUE_WHALE': {
        'name': 'Whale',
        'stats': {
            'health': lambda lvl: lvl * 2
        },
        'ability': _bluewhale,
        'type': 'fishing',
    },
    'GIRAFFE': {
        'name': 'Giraffe',
        'stats': {
            'health': lambda lvl: lvl,
            'crit chance': lambda lvl: lvl / 20
        },
        # Grants (Pet lvl * 0.4) strength and (20 + (Pet lvl * 0.1)) crit damage when mid air. (Rare)
        # ((Pet lvl * 0.5) strength and (20 + (Pet lvl * 0.25)) crit damage on Epic)
        # ((Pet lvl * 0.5) strength and (20 + (Pet lvl * 0.4)) crit damage on Legendary)
        'ability': None,
        'type': 'foraging',
    },
    'PHOENIX': {
        'name': 'Phoenix',
        'stats': {
            'strength': lambda lvl: (lvl / 2) + 10,
            'intelligence': lambda lvl: lvl + 50
        },
        # Before death, become immune and gain (10 + (Pet lvl * 0.1)) strength on (2 + (Pet lvl * 0.02)) seconds (3 minutes cooldown). (Epic)
        # ((10 + (Pet lvl * 0.2) STR on (2 + (Pet lvl * 0.02)) seconds on Legendary)
        # On 4th melee strike, ignite mobs, dealing (1 + (Pet lvl * 0.14)) your crit damage each second for (2 + (Pet lvl/25)) seconds. (Epic, Legendary)
        'ability': None,
        'type': 'combat',
    },
    'BEE': {
        'name': 'Bee',
        'stats': {
            'intelligence': lambda lvl: lvl / 2,
            'strength': lambda lvl: (lvl / 4) + 5,
            'speed': lambda lvl: lvl / 10,
        },
        # Gain (1 + (Pet lvl * 0.02)) Intelligence and (1 + (Pet lvl * 0.02)) Strength for each nearby bee. (Max 15) (Common)
        # (1+ (Pet lvl * 0.09) INT and (1 + (Pet lvl * 0.07)) STR on Rare)
        # (1+ (Pet lvl * 0.14) INT and (1 + (Pet lvl * 0.11)) STR on Epic)
        # (1+ (Pet lvl * 0.19) INT and (1 + (Pet lvl * 0.14)) STR on Legendary)
        'ability': _bee,
        'type': 'farming',
    },
    'MAGMA_CUBE': {
        'name': 'Magma Cube',
        'stats': {
            'strength': lambda lvl: lvl / 5,
            'defense': lambda lvl: lvl / 3,
            'health': lambda lvl: lvl / 2
        },
        # Deal (Pet lvl * 0.25%) more damage to slimes. (Rare, Epic, Legendary)
        # Buffs the stats of Ember Armor by (Pet lvl * 1%). (Legendary)
        'ability': _magmacube,
        'type': 'combat',
    },
    'FLYING_FISH': {
        'name': 'Flying Fish',
        'stats': {
            'strength': lambda lvl: lvl / 2,
            'defense': lambda lvl: lvl / 2
        },
        # Gives (Pet lvl * 0.4) strength when near water. (Rare) (0.5 on Epic, Legendary)
        # Increases the stats of Diver's Armor by (Pet lvl * 0.3%). (Legendary)
        'ability': _flyingfish,
        'type': 'fishing',
    },
    'SQUID': {
        'name': 'Squid',
        'stats': {
            'intelligence': lambda lvl: lvl / 2,
            'health': lambda lvl: lvl / 2
        },
        # Buffs the Ink Wand by (Pet lvl * 0.3) damage and (Pet lvl * 0.1) strength. (Rare) (0.4 DMG and 0.2 STR on Epic, Legendary)
        'ability': _squid,
        'type': 'fishing',
    },
    'PARROT': {
        'name': 'Parrot',
        'stats': {
            'crit damage': lambda lvl: lvl / 10,
            'intelligence': lambda lvl: lvl
        },
        # Gives (5 + (Pet lvl * 0.25)) strength to profiles within 20 Blocks (No stack). (Legendary)
        'ability': _parrot,
        'type': 'alchemy',
    },
    'TIGER': {
        'name': 'Tiger',
        'stats': {
            'strength': lambda lvl: (lvl / 10) + 5,
            'crit chance': lambda lvl: lvl / 20,
            'crit damage': lambda lvl: lvl / 2
        },
        # Attacks have a (Pet lvl * 0.05%) chance to strike twice. (Common) (0.1% on Uncommon, Rare) (0.2% on Epic, Legendary)
        # Deal (Pet lvl * 0.2%) more damage against targets with no other mobs within 15 blocks. (Legendary)
        'ability': None,
        'type': 'combat',
    },
    'TURTLE': {
        'name': 'Turtle',
        'stats': {
            'health': lambda lvl: lvl / 2,
            'defense': lambda lvl: lvl
        },
        'ability': _turtle,
        'type': 'combat',
    },
    'BLAZE': {
        'name': 'Blaze',
        'stats': {
            'intelligence': lambda lvl: lvl,
            'defense': lambda lvl: (lvl / 5) + 10
        },
        # Upgrades Blaze Armor stats and ability by (Pet lvl * 0.4%). (All)
        # Double effects of Hot Potato Books. (Legendary)
        'ability': _blaze,
        'type': 'combat',
    },
    'JERRY': {
        'name': 'Jerry',
        'stats': {
            'intelligence': lambda lvl: -lvl
        },
        'ability': _jerry,
        'type': 'combat',
    },
    'ZOMBIE': {
        'name': 'Zombie',
        'stats': {
            'crit damage': lambda lvl: lvl * 0.3,
            'health': lambda lvl: lvl
        },
        # Deal (Pet lvl * 0.2%) more damage to zombies. (Epic, Legendary)
        'ability': _zombie,
        'type': 'combat',
    },
    'DOLPHIN': {
        'name': 'Dolphin',
        'stats': {
            'intelligence': lambda lvl: lvl,
            'sea creature chance': lambda lvl: lvl / 20
        },
        'ability': _dolphin,
        'type': 'fishing',
    },
    'JELLYFISH': {
        'name': 'Jellyfish',
        'stats': {
            'health': lambda lvl: lvl * 2
        },
        'ability': None,
        'type': 'alchemy',
    },
    'ELEPHANT': {
        'name': 'Elephant',
        'stats': {
            'health': lambda lvl: lvl,
            'intelligence': lambda lvl: lvl * 0.75
        },
        'ability': _elephant,
        'type': 'farming',
    },
    'MONKEY': {
        'name': 'Monkey',
        'stats': {
            'speed': lambda lvl: lvl / 5,
            'intelligence': lambda lvl: lvl / 2
        },
        'ability': None,
        'type': 'foraging',
    },
    'SKELETON': {
        'name': 'Skeleton',
        'stats': {
            'crit chance': lambda lvl: lvl * 0.15,
            'crit damage': lambda lvl: lvl * 0.3
        },
        # Increase arrow damage by (Pet lvl * 0.1%), which is tripled while in dungeons. (Common, Uncommon, Rare) (0.2% on Epic, Legendary)
        # Gain a combo stack for every bow hit granting +3 Strength. Max (Pet lvl * 0.1) stacks, stacks disappear after 8 seconds. (Rare) (0.2 on Epic, Legendary)
        'ability': None,
        'type': 'combat',
    },
    'SPIDER': {
        'name': 'Spider',
        'stats': {
            'strength': lambda lvl: lvl / 10,
            'crit chance': lambda lvl: lvl / 10
        },
        # Gain (Pet lvl * 0.1) strength for every nearby spider (Max 10). (All)
        'ability': None,
        'type': 'combat',
    },
    'ENDERMITE': {
        'name': 'Endermite',
        'stats': {
            'intelligence': lambda lvl: lvl
        },
        'ability': None,
        'type': 'mining',
    },
    'PIG': {
        'name': 'Pig',
        'stats': {
            'speed': lambda lvl: lvl / 4
        },
        'ability': None,
        'type': 'farming',
    },
    'ROCK': {
        'name': 'Rock',
        'stats': {
            'defense': lambda lvl: lvl * 2,
            'true defense': lambda lvl: lvl / 10
        },
        # While sitting on your rock, gain (Pet lvl * 0.3%) more damage. (Legendary)
        'ability': None,
        'type': 'mining',
    },
    'HOUND': {
        'name': 'Hound',
        'stats': {
            'strength': lambda lvl: lvl * 0.4,
            'attack speed': lambda lvl: lvl * 0.15
        },
        'ability': _hound,
        'type': 'combat',
    },
    'GHOUL': {
        'name': 'Ghoul',
        'stats': {
            'health': lambda lvl: lvl,
            'intelligence': lambda lvl: lvl * 0.7
        },
        'ability': None,
        'type': 'combat',
    },
    'TARANTULA': {
        'name': 'Tarantula',
        'stats': {
            'strength': lambda lvl: lvl / 10,
            'crit chance': lambda lvl: lvl / 10,
            'crit damage': lambda lvl: lvl * 0.3
        },
        'ability': None,
        'type': 'combat',
    },
    'GOLEM': {
        'name': 'Golem',
        'stats': {
            'strength': lambda lvl: lvl / 2,
            'health': lambda lvl: lvl * 1.5
        },
        # While less than 15% HP, deal (Pet lvl * 0.3%) more damage. (All)
        'ability': None,
        'type': 'combat',
    },
    'BLACK_CAT': {
        'name': 'Black Cat',
        'stats': {
            'intelligence': lambda lvl: lvl,
            'speed': lambda lvl: lvl / 4
        },
        'ability': _blackcat,
        'type': 'combat',
    },
    'BABY_YETI': {
        'name': 'Baby Yeti',
        'stats': {
            'strength': lambda lvl: lvl * 2 / 5
        },
        'ability': _yeti,
        'type': 'fishing',
    },
    'SPIRIT': {
        'name': 'Spirit',
        'stats': {
            'speed': lambda lvl: lvl * 0.3,
            'intelligence': lambda lvl: lvl
        },
        'ability': None,
        'type': 'combat',
    },
    'GRIFFIN': {
        'name': 'Griffin',
        'stats': {
            'crit chance': lambda lvl: lvl / 10,
            'crit damage': lambda lvl: lvl / 2,
            'strength': lambda lvl: lvl / 4,
            'magic find': lambda lvl: lvl / 10,
            'intelligence': lambda lvl: lvl / 10
        },
        'ability': None,
        'type': 'combat'
    }
}
