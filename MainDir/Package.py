import sys
import os
import asyncio
sys.path.insert(0,os.path.dirname(os.path.realpath(__file__)) + "/..")
import Utils
class Package:
    name = ""
    db = None
    LocalisationReference = None

    def getText(self, id, value):
        return self.LocalisationReference.getText(self.name, value, Utils.getChannelLanguage(self.db, id))

    def getDescription(self, channelID):
        return self.LocalisationReference.getText(self.name, "description", Utils.getChannelLanguage(self.db, channelID))
    
    def getAdditionalUserValues(self):
        return None
    def getAdditionalGuildvalues(self):
        return None

    def GiveDataBaseReference(self, db):
        self.db = db

    def getUpdateFunctions(self):
        return None

    def getCommands(self):
        return None

    def getAdditionalGuildValues(self):
        return None

    async def on_raw_message_delete(payload):
        pass
    async def on_message_edit(before, after):
        pass
    async def on_reaction_add(reaction, user):
        pass
    async def on_raw_reaction_add(payload):
        pass
    async def on_reaction_remove(reaction, user):
        pass
    async def on_raw_reaction_remove(payload):
        pass
    async def on_reaction_clear(message, reactions):
        pass
    async def on_raw_reaction_clear(payload):
        pass
    async def on_private_channel_delete(channel):
        pass
    async def on_private_channel_create(channel):
        pass
    async def on_private_channels_update(before, after):
        pass
    async def on_private_channel_pins_update(channel, last_pin):
        pass
    async def on_guild_channel_delete(channel):
        pass
    async def on_guild_channel_create(channel):
        pass
    async def on_guild_channel_update(before, after):
        pass
    async def on_guild_channel_pins_update(channel, last_pin):
        pass
    async def on_guild_integrations_update(guild):
        pass
    async def on_webhoooks_update(channel):
        pass
    async def on_member_join(member):
        pass
    async def on_member_remove(member):
        pass
    async def on_member_update(before, after):
        pass
    async def on_guild_join(guild):
        pass
    async def on_guild_remove(guild):
        pass
    async def on_guild_update(guild):
        pass
    async def on_guild_role_create(role):
        pass
    async def on_guild_role_delete(role):
        pass
    async def on_guild_role_update(before, after):
        pass
    async def on_guild_emojis_update(guild, before, after):
        pass
    async def on_voice_state_update(member, before, after):
        pass
    async def on_member_ban(guild, user):
        pass
    async def on_member_unban(guild, user):
        pass