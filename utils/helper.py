import asyncio
import aiohttp
import time
import re
from copy import deepcopy
from urllib.parse import quote

from lib import Guild, ExternalAPIError, BadNameError, BadGuildError
from . import Embed
from constants import MOBS_RELEVANT_ENCHANTS, ENCHANTMENT_BONUS, STAT_NAMES, SKILL_NAMES, SLAYER_NAMES
from constants.discord import TIMEOUT_EMOJIS
from constants.db_schema import GUILD_CONFIG


async def get_uuid_from_name(name, *, session):
    try:
        async with session.get(f'https://api.mojang.com/users/profiles/minecraft/{name}') as resp:
            if resp.status == 204:
                raise BadNameError(name) from None

            json = await resp.json(content_type=None)

            if json is None or 'name' not in json or 'id' not in json:
                raise BadNameError(name) from None

            return json['name'], json['id']
    except (asyncio.TimeoutError, aiohttp.ClientConnectorError):
        raise ExternalAPIError('Could not connect to https://api.mojang.com.') from None
    except aiohttp.ClientResponseError as e:
        if e.status == 429:
            raise ExternalAPIError('Mojang API ratelimit has been reached!') from None
        else:
            raise BadNameError(name) from None


async def get_name_from_uuid(uuid, *, session):
    try:
        async with session.get(f'https://api.mojang.com/user/profiles/{uuid}/names') as resp:
            if resp.status == 204:
                raise BadNameError(uuid) from None

            json = await resp.json(content_type=None)
            if json is None:
                raise BadNameError(uuid) from None

            return json
    except (asyncio.TimeoutError, aiohttp.ClientConnectorError):
        raise ExternalAPIError('Could not connect to https://api.mojang.com.') from None
    except aiohttp.ClientResponseError as e:
        if e.status == 429:
            raise ExternalAPIError('Mojang API ratelimit has been reached!') from None
        else:
            raise BadNameError(uuid) from None


def level_from_xp_table(xp, table):
    """
    Takes a xp value and a list of level requirements.
    Returns whatever level the thing should be at.
    """
    level = 0
    for i, requirement in enumerate(table):
        if xp >= requirement:
            level = i + 1
        else:
            break
    return level


def safe_list_get(lst, i):
    try:
        return lst[i]
    except IndexError:
        return None


def damage(weapon_dmg, strength, crit_dmg, ench_modifier):
    return (5 + weapon_dmg + strength // 5) * (1 + strength / 100) * (1 + crit_dmg / 100) * (1 + ench_modifier / 100)


async def get_item_price_stats(item_id, *, session):
    """
    Get item's price stats with item id.
    """
    try:
        async with session.get(f'https://auctions.craftlink.xyz/api/items/{item_id}/quickStats') as response:
            json = await response.json(content_type=None)
            if json is None or 'success' not in json:
                return None
            if not json['success']:
                return None
            return json['data']
    except asyncio.TimeoutError:
        raise ExternalAPIError('Could not connect to https://auctions.craftlink.xyz.') from None


async def get_item_list(item_name, *, session):
    """
    Search with item name and return the first result's item id.
    """
    item_name = quote(item_name)
    try:
        async with session.get(f'https://auctions.craftlink.xyz/api/items/search?name={item_name}') as response:
            json = await response.json(content_type=None)
            if json is None or 'success' not in json:
                return None
            if not json['success']:
                return None
            return json['data']
    except asyncio.TimeoutError:
        raise ExternalAPIError('Could not connect to https://auctions.craftlink.xyz.') from None


def colorize(s, color):
    language, point = color
    s = str(s)
    if not s:
        return ''
    return f'```{language}\n{point}' + s.replace('\n', f'\n{point}') + '\n```'


def format_pet(pet):
    return f'{pet.title} |{pet.rarity.upper()}|' if pet else ''


async def embed_timeout_handler(ctx, emoji_list, message=None):
    message = message or ctx.message
    try:
        await message.clear_reactions()
        for emoji in TIMEOUT_EMOJIS:
            await message.add_reaction(emoji)
    except Exception:
        try:
            for (emoji, _) in emoji_list:
                await message.remove_reaction(emoji, ctx.bot.user)
            for emoji in TIMEOUT_EMOJIS:
                await message.add_reaction(emoji)
        except Exception:
            pass


def emod(activity, weapon):
    result = 0
    for enchantment in MOBS_RELEVANT_ENCHANTS[activity]:
        if enchantment in weapon.enchantments:
            value = ENCHANTMENT_BONUS[enchantment]
            if callable(value):
                result += value(weapon.enchantments[enchantment])
            else:
                result += value * weapon.enchantments[enchantment]
    return result


def get_stats_from_description(desc, *, dungeon=False):
    """
    Get item stats from clean description and estimated total dungeon bonus.
    Return item stats dict, item reforge stats dict, estimated total dungeon bonus value.
    """
    stat_regex = re.compile('([\w ]*): \D?(\d*\.?\d*)(.*)')
    reforge_regex = re.compile('.*\(([\w ]*) \+(\d*)')
    dungeon_regex = re.compile('.*\(\D?(\d*\.\d*).*\)')
    stats = {}
    reforge_stats = {}
    dungeon_bonus = 1.00
    for line in desc:
        stat_match = stat_regex.match(line)
        if stat_match is None:
            continue  # if doesn't match

        stat_type = stat_match.group(1).lower()
        stat_value = stat_match.group(2)
        if not stat_value or not stat_type:
            continue
        stat_value = float(stat_value)

        if stat_type in STAT_NAMES:
            if stat_type == 'bonus attack speed':
                stat_type = 'attack speed'  # remove bonus
            stats[stat_type] = stat_value

        # check for reforge stat
        if stat_match.group(3):
            reforge_match = reforge_regex.match(stat_match.group(3))
            if reforge_match is not None:
                reforge_value = reforge_match.group(2)

                if reforge_value:
                    reforge_value = float(reforge_value)
                    reforge_stats[stat_type] = reforge_value

            if dungeon and stat_type not in ('crit chance', 'attack speed'):
                dungeon_match = dungeon_regex.match(stat_match.group(3))
                if dungeon_match is None:
                    continue

                dungeon_stat = dungeon_match.group(1)
                if not dungeon_stat:
                    continue
                dungeon_stat = float(dungeon_stat)

                if dungeon_stat < stat_value:
                    continue  # if the matched stat is less than main stat

                dungeon_bonus = float(dungeon_stat / stat_value)

    return stats, reforge_stats, dungeon_bonus


def closest(lst, k):
    """
    Find closest number in the given list.
    Return the number and the index in that list
    """
    num = min(range(len(lst)), key=lambda i: abs(lst[i] - k))
    return lst[num], num


async def ask_for_skyblock_profiles(ctx, player, profile, *, session, hypixel_api_client, auto_set=False,
                                    get_guild=False):
    if not player:
        player = await ctx.ask(message=f'{ctx.author.mention}, What is your minecraft username?')

    player_name, player_uuid = await get_uuid_from_name(player, session=session)
    player = await hypixel_api_client.get_player(player_uuid, uname=player_name)

    if profile:
        await player.load_skyblock_profiles(selected_profile=profile)
    else:
        await player.load_skyblock_profiles()

    if auto_set:
        player.profile.set_pet_armor_automatically()

    if get_guild:
        await player.get_player_guild()

    return player


async def ask_for_guild(ctx, guild, *, hypixel_api_client, load_members=False):
    if not guild:
        guild = await ctx.ask(message=f'{ctx.author.mention}, What is the guild you want to check?')

    guild_data = await hypixel_api_client.get_guild(params={'name': quote(guild)})
    if guild_data is None:
        raise BadGuildError(guild)
    await ctx.send(f'{ctx.author.mention}, I am getting the guild information, please wait a little bit!')

    guild = Guild(guild_data)

    if load_members:
        await guild.load_all_members(hypixel_api_client=hypixel_api_client)

    return guild


def get_guild_leaderboard(guild):
    all_leaderboard = {}

    # Skill average leaderboard
    skill_average_leaderboard = sorted(guild.all_members_skill_average, reverse=True,
                                       key=lambda member: guild.all_members_skill_average[member])
    skill_average_leaderboard = [
        f'#{str(i + 1).ljust(3)} {member} > {guild.all_members_skill_average[member]:.2f}' for i, member in
        enumerate(skill_average_leaderboard)]
    all_leaderboard['Skill Average'] = skill_average_leaderboard

    # Unique minions leaderboard
    unique_minions_leaderboard = sorted(guild.all_members_unique_minions, reverse=True,
                                        key=lambda member: guild.all_members_unique_minions[member])
    unique_minions_leaderboard = [
        f'#{str(i + 1).ljust(3)} {member} > {guild.all_members_unique_minions[member]} '
        f'[{guild.all_members_minion_slots[member]}]' for i, member in enumerate(unique_minions_leaderboard)]
    all_leaderboard['Unique Minions'] = unique_minions_leaderboard

    # Skill leaderboards
    for skill in SKILL_NAMES:
        skill_leaderboard = sorted(guild.all_members_skills_xp, reverse=True,
                                   key=lambda member: guild.all_members_skills_xp[member].get(skill, 0))
        skill_leaderboard = [
            f'#{str(i + 1).ljust(3)} {member} > {guild.all_members_skills_xp[member].get(skill, 0):,.0f} '
            f'[{guild.all_members_skills[member].get(skill, 0)}]' for i, member in
            enumerate(skill_leaderboard)]
        all_leaderboard[skill] = skill_leaderboard

    # Slayer leaderboards
    for slayer in SLAYER_NAMES:
        slayer_leaderboard = sorted(guild.all_members_slayers_xp, reverse=True,
                                    key=lambda member: guild.all_members_slayers_xp[member].get(slayer, 0))
        slayer_leaderboard = [
            f'#{str(i + 1).ljust(3)} {member} > {guild.all_members_slayers_xp[member].get(slayer, 0):,.0f} '
            f'[{guild.all_members_slayers[member].get(slayer, 0)}]' for i, member in
            enumerate(slayer_leaderboard)]
        all_leaderboard[slayer] = slayer_leaderboard

    # Total slayer xp leaderboard
    total_slayer_xp_leaderboard = sorted(guild.all_members_total_slayers_xp, reverse=True,
                                         key=lambda member: guild.all_members_total_slayers_xp[member])
    total_slayer_xp_leaderboard = [
        f'#{str(i + 1).ljust(3)} {member} > {guild.all_members_total_slayers_xp[member]:,.0f}' for i, member in
        enumerate(total_slayer_xp_leaderboard)]
    all_leaderboard['Total Slayer XP'] = total_slayer_xp_leaderboard

    # Dungeon level leaderboard
    dungeon_level_leaderboard = sorted(guild.all_members_dungeon_level, reverse=True,
                                       key=lambda member: guild.all_members_dungeon_level[member])
    dungeon_level_leaderboard = [f'#{str(i + 1).ljust(3)} {member} > Level {guild.all_members_dungeon_level[member]}'
                                 for i, member in enumerate(dungeon_level_leaderboard)]
    all_leaderboard['Dungeon Level'] = dungeon_level_leaderboard

    return all_leaderboard


async def get_event_estimate_time(endpoint, *, session):
    try:
        async with session.get(f'https://hypixel-api.inventivetalent.org/api/{endpoint}') as resp:
            json = await resp.json(content_type=None)
            if json is None or 'success' not in json:
                return None
            if not json['success']:
                return None
            return json['estimate']
    except asyncio.TimeoutError:
        raise ExternalAPIError('Could not connect to https://hypixel-api.inventivetalent.org.') from None


def current_milli_time():
    return int(round(time.time() * 1000.0))


async def get_guild_config(guild_db, *, ctx=None, guild=None, safe=True):
    if guild is None:
        guild = ctx.guild
        if guild is None:
            return None

    guild_config = await guild_db.find_one({'_id': guild.id})

    if guild_config is None:
        if not safe:
            return None
        guild_config = deepcopy(GUILD_CONFIG)

        guild_config['_id'] = guild.id
        guild_config['name'] = guild.name
        guild_config['icon'] = str(guild.icon_url)
        guild_config['banner'] = str(guild.banner_url)
        guild_config['last_updated'] = int(time.time())

        await guild_db.insert_one(guild_config)

    return guild_config


async def send_no_permission_embed(ctx):
    return await Embed(
        ctx=ctx,
        title='Command Error',
        description='Sorry, it looks like I don\'t have the permissions or roles to do that.\n'
                    'Try enabling your DM or contract the server owner to give me more permissions.'
    ).send()
