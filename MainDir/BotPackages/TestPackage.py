import sys
import time
import asyncio
import os

def getChannelLanguage(db, channelID):
    a = db.SELECT("ChannelsAndLanguages",["language"], "channelID = " + str(channelID))
    if len(a) == 0:
        db.INSERT("ChannelsAndLanguages", [["language", "en-EN"], ["channelID", str(channelID)]])
        return "en-EN"
    return a[0][0]

class Package:
    name = "TestPackage"
    db = None
    LocalisationReference = None

    def __init__(self, LocalisationReference):
        self.LocalisationReference = LocalisationReference
        print("Package initialized")
    
    def getDescription(self, channelID):
        return self.LocalisationReference.getText(self.name, "description", getChannelLanguage(self.db, channelID))

    def getUpdateFunctions(self):
        return None
    
    def getCommands(self):
        return [
            ["help", self.help],
            ["test", self.test_function],
        ]

    def getAdditionalGuildValues(self):
        return [
            ["TestPackageLanguage", "string"]
        ]

    def getAdditionalUserValues(self):
        return [
            ["TestPackageHelpDelay", "int"],
            ["TestPackageTestFunctionDelay", "int"]
        ]

    def GiveDataBaseReference(self, db):
        self.db = db
        try:
            db.CREATE_TABLE("ChannelsAndLanguages", [["channelID", "string"], ["language", "string"]])
        except:
            pass

    async def help(self, params, message, client):
        if self.db is not None:
            data = self.db.GetUserData(message.author.id)


            print(data)


        await message.channel.send(self.LocalisationReference.getText(self.name, "help", getChannelLanguage(self.db, message.channel.id)))



    async def test_function(self, params, message, client):
        if self.db is not None:
            data = self.db.GetUserData(message.author.id)


            print(data)


        await message.channel.send(self.LocalisationReference.getText(self.name, "test", getChannelLanguage(self.db, message.channel.id)))