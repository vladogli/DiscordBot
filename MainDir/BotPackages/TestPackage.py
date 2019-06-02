import sys
import time
import asyncio
class Package:
    name = "TestPackage"
    description = "That's just a test package."
    db = None
    def __init__(self):
        print("Package initialized")
    async def help(self, message, client):
        if db is not None:
            data = db.GetUserData(message.client.id)


            print(data)


        await message.channel.send("this is help")



    async def test_function(self, message, client):
        if db is not None:
            data = db.GetUserData(message.client.id)


            print(data)


        await message.channel.send("this is test")



    async def updateFunction1(self):
        while True:
            print("updating....")
            await asyncio.sleep(1)
    async def updateFunction2(self):
        while True:
            print("updating2....")
            await asyncio.sleep(1)
    def getCommands(self):
        return [
            ["help", self.help],
            ["test", self.test_function]
        ]
    
    def getUpdateFunctions(self):
        return [
            self.updateFunction1,
            self.updateFunction2
        ]
    def getAdditionalGuildValues(self):
        return None
    def getAdditionalUserValues(self):
        return [
            ["TestPackageHelpDelay", "int"],
            ["TestPackageTestFunctionDelay", "int"]
        ]
    def GiveDataBaseReference(self, db):
        self.db = db