GUILD_CONFIG = {
    '_id': None,
    'name': None,
    'icon': None,
    'banner': None,
    'visible': True,
    'reports_enabled': True,
    'global_blacklisted': False,
    'global_blacklisted_commands': [],
    'restricted_commands': [],
    'events': {
        'default_enabled': True,
        'default_mention_id': None,
        'default_webhook_data': None,
        'magmaBoss': {
            'enabled': False,
            'mention_id': None,
            'webhook_data': None
        },
        'darkAuction': {
            'enabled': False,
            'mention_id': None,
            'webhook_data': None
        },
        'bankInterest': {
            'enabled': False,
            'mention_id': None,
            'webhook_data': None
        },
        'newYear': {
            'enabled': False,
            'mention_id': None,
            'webhook_data': None
        },
        'zoo': {
            'enabled': False,
            'mention_id': None,
            'webhook_data': None
        },
        'spookyFestival': {
            'enabled': False,
            'mention_id': None,
            'webhook_data': None
        },
        'winterEvent': {
            'enabled': False,
            'mention_id': None,
            'channel_id': None,
            'webhook_data': None
        },
        'jerryWorkshopEvent': {
            'enabled': False,
            'mention_id': None,
            'webhook_data': None
        }
    },
    'last_updated': None
}

PLAYER_DATA = {
    'mojang_uuids': [],
    'discord_ids': [],
    'global_blacklisted': False,
    'guild_report_blacklisted': [],
    'guild_reputation_blacklisted': [],
}

REPUTATION = {
    'guild_id': None,
    'reported_discord_id': None,
    'submitter_discord_id': None,
    'reason': '',
    'positive': True,
    'type': None,
    'staff_sorted_discord_id': None,
    'submitted_timestamp': None
}

REP_CATEGORY = {
    'guild_id': None,
    'name': None,
    'description': '',
    'enabled': True
}

REPORT = {
    'guild_id': None,
    'reported_discord_id': None,
    'reported_mojang_uuid': None,
    'submitter_discord_id': None,
    'submitter_mojang_uuid': None,
    'reason': None,
    'proof': None,
    'staff_verified_discord_id': None,
    'staff_note': None,
    'submitted_timestamp': None
}

DISCORD_USERNAME = {
    '_id': None,
    'current_name': None,
    'name_history': [],
    'updated_timestamp': None
}
