import sys
import os
import importlib.util
FOLDER_PATH = os.path.dirname(os.path.realpath(__file__)) + "/BotPackages/"
Packages = []
newScript = open("generated_script.py","w+")
newScript.write("import sys\nimport os\n")
newScript.write("sys.path.insert(0,os.path.dirname(os.path.realpath(__file__)) + \"/BotPackages/\")\n")
newScript.write("massive = [] \n")
for file in ([f for f in os.listdir(FOLDER_PATH) if os.path.isfile(os.path.join(FOLDER_PATH, f))]):
    newScript.write("import " + file[0:file.find(".")] + "\n")
    newScript.write("massive.append(" + file[0:file.find(".")] + ".Package)\n")
newScript.close()

import Core