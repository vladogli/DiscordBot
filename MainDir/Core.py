import sys
import os
sys.path.insert(0,os.path.dirname(os.path.realpath(__file__)) + "/DataBases/")
import discord
import asyncio
import generated_script
import time
import DataBase
import json
import Utils
plugins = []

sys.path.insert(0,os.path.dirname(os.path.realpath(__file__)) + "/localisation/")
import localisation
Localisation = localisation.Localisation()

client = discord.Client()
for plugin in generated_script.massive:
    g = plugin(Localisation)
    plugins.append(g)
    val = g.getUpdateFunctions()
    if val is not None:
        for function in val:
            client.loop.create_task(function())

db = DataBase.DB(plugins)




async def addGuild(id):
    enabled_plugins = "{"
    for plugin in plugins:
        enabled_plugins += "\"" + plugin.name + "\": []"
    enabled_plugins += "}"
    db.AddGuild(id, "!", enabled_plugins)

async def admin_message(command, message, client, guildData):
    lang =  Utils.getChannelLanguage(db, message.channel.id)
    print(lang)
    def lGetText(value):
            return Localisation.getText("AdminCommands", value, lang)
    if(command[0] == "help"):
        embed = discord.Embed(
            title = lGetText("helpTitle"),
            color = 0xff0000)
        embed.add_field(name="help", value=lGetText("help"), inline=False)
        embed.add_field(name="listOfPackages", value=lGetText("listOfPackages"), inline=False)
        embed.add_field(name=lGetText("connectPackageCmd"), value=lGetText("connectPackage"), inline=False)
        embed.add_field(name=lGetText("disconnectPackageCmd"), value=lGetText("disconnectPackage"), inline=False)
        embed.add_field(name="listOfLanguages", value=lGetText("listOfLanguages"), inline=False)
        embed.add_field(name=lGetText("changeLanguageCmd"), value=lGetText("changeLanguage"), inline=False)
        await message.channel.send(embed=embed)
    elif command[0] == "listofpackages":
        embed = discord.Embed(
            title = lGetText("listOfPackagesTitle"),
            color = 0xaa00aa)
        for plugin in plugins:
            embed.add_field(name=plugin.name, value=plugin.getDescription(message.channel.id), inline=True)
        await message.channel.send(embed=embed)
    elif command[0] == "connectpackage":
        plugin_channels = json.loads(guildData[0][2])
        try:
            for element in plugin_channels[command[1][0]]:
                if element == message.channel.id:
                    await message.channel.send(lGetText("connectPackageFail"))
                    return
            plugin_channels[command[1][0]].append(message.channel.id)
        except:
            await message.channel.send(lGetText("connectPackageFailWN"))
            return       
        db.EditGuild(message.guild.id, guildData[0][1], json.dumps(plugin_channels))

        await message.channel.send(lGetText("connectPackageSuccess"))
    elif command[0] == "disconnectpackage":
        plugin_channels = json.loads(guildData[0][2])
        try:
            for element in plugin_channels[command[1][0]]:
                if element == message.channel.id:
                    plugin_channels[command[1][0]].remove(element)
                    db.EditGuild(message.guild.id, guildData[0][1], json.dumps(plugin_channels))
                    await message.channel.send(lGetText("disconnectPackageSuccess"))
                    return
        except:
            await message.channel.send(lGetText("connectPackageFailWN"))
        await message.channel.send(lGetText("disconnectPackageFail"))
    elif command[0] == "listoflanguages":
        embed = discord.Embed(
            title = lGetText("listOfAvailableLanguagesTitle"),
            color = 0x880088)
        for element in Localisation.getAvailableLanguages():
            embed.add_field(name=element, value=Localisation.getText("description", "name", element), inline=True)
        await message.channel.send(embed=embed)
    elif command[0] == "changelanguage":
        for element in Localisation.getAvailableLanguages():
            if element == command[1][0]:
                db.UPDATE("ChannelsAndLanguages", [["language", element]], "channelID = " + str(message.channel.id))
                await message.channel.send(lGetText("changeLanguageSuccess"))
                return
        await message.channel.send(lGetText("changeLanguageWL"))
@client.event
async def on_message(message):
    if(message.author == client.user):
        return
    data = db.GetGuildData(message.guild.id)
    if len(data) == 0:
        await addGuild(message.guild.id)
        return
    if message.content[0]!=data[0][1]:
        return
    command = Utils.getCommand(message.content)
    Plugins = json.loads(data[0][2])
    for Plugin in Plugins:
        for channel in Plugins[Plugin]:
            if channel == message.channel.id:
                for plugin in plugins:
                    if plugin.name == Plugin:
                        for Command in plugin.getCommands():
                            if Command[0] == command[0]:
                                await Command[1](command[1], message, client)
                                return
    if message.author.permissions_in(message.channel).value & 8 == 8:
        await admin_message(command, message, client, data)




f = open('token')
token = f.readline()
f.close()
client.run(token)