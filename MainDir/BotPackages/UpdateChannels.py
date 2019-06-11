import sys
import time
import asyncio
import os
import discord
sys.path.insert(0,os.path.dirname(os.path.realpath(__file__)) + "/..")
import Utils
import Package as pckg

class Package(pckg.Package):
    name = "UpdateChannels"

    def __init__(self, LocalisationReference):
        self.LocalisationReference = LocalisationReference

    def getCommands(self):
        return [
            ["help", self.help],
            ["addchannel", self.addChannel],
            ["viewchannels", self.viewChannels],
            ["removechannel", self.removeChannel],
        ]
    
    async def help(self, params, message, client):
        embed = discord.Embed(
            title = self.getText("helpTitle"),
            color = 0xff84ff)
        embed.add_field(name="help", value= self.getText("help"), inline=False)
        embed.add_field(name="addChannel", value= self.getText("addChannel"), inline=False) 
        embed.add_field(name="viewChannels", value= self.getText("viewChannels"), inline=False) 
        embed.add_field(name="removeChannel", value= self.getText("removeChannel"), inline=False)  
        await message.channel.send(embed=embed)

    async def 
    async def addChannel(self, params, message, client):
        try:
            channels = (db.SELECT("UpdateChannelsChannels", ["channels"], "guildID = " message.guild.id)))
            if len(channels) == 0:
                
            else:
                jsonChannels = json.loads(channels[0])
                if jsonChannels[params[0]] != 0:

                    return
                channel = discord.find(lambda m: str(m.id) == params[0], message.guild.voice_channels)
                if len(channel) == 0:
                    await message.channel.send(self.getText("addChannelFailAC"))
                    return
        except:
            await message.channel.send(self.getText("addChannelFail"))
            return
        db.INSERT("UpdateChannelsChannels", [str(params[0]), str(channel[0].user_limit)])


    async def removeChannel(self, params, message, client):
        pass

    async def viewChannels(self, params, message, client):

    def GiveDataBaseReference(self, db):
        self.db = db
        try:
            db.CREATE_TABLE("UpdateChannelsChannels", [["guildID", "string"],["channels", "str"]])
        except:
            pass