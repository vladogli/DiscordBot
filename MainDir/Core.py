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

client = discord.Client()
for plugin in generated_script.massive:
    g = plugin()
    plugins.append(g)
    for function in g.getUpdateFunctions():
        client.loop.create_task(function())

db = DataBase.DB(plugins)






async def addGuild(id):
    enabled_plugins = "{"
    for plugin in plugins:
        enabled_plugins += "\"" + plugin.name + "\": [0]"
    enabled_plugins += "}"
    db.AddGuild(id, "!", enabled_plugins)
async def admin_message(command):
    pass

@client.event
async def on_message(message):
    if(message.author == client.user):
        return
    
    data = db.GetGuildData(message.guild.id)
    if len(data) == 0:
        await addGuild(message.guild.id)
        return
    if message.content[0]!=data[1]:
        print(data[1])
        print(message.content[0])
        return
    command = Utils.getCommand(message.content)
    msg = message.content[1:]
    Plugins = json.loads(data[2])
    for Plugin in Plugins:
        for channel in Plugins[Plugin]:
            if channel == message.channel.id:
                for plugin in plugins:
                    if plugin.Name == Plugin:
                        for command in plugin.getCommands():
                            if command[0] == msg:
                                command[1](message, client)
                                return
    print(message.author.permissions_in(message.channel))




f = open('token')
token = f.readline()
f.close()
client.run(token)