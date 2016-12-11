# Dice Roll of Scripts in Chosen Folder
import os
import random
import subprocess
import sys

# Check For Admin PermissionS
if not os.geteuid() == 0:
    sys.exit('Script must be run as root')

# List Folders In a Directory and Make a Choice
directoryList = sorted(filter(os.path.isdir, os.listdir('.')))
directories = str("")

for directory in directoryList:
    if directories != "":
        directories += ", "
    directories += "[" + directory + "]"
print("List-O-Folders: " + directories)
folderChoice = str(input("Pick-A-Folder : "))

# Change Directory To Choice
if os.path.isdir(os.getcwd() + os.path.sep + folderChoice):
    os.chdir(os.getcwd() + os.path.sep + folderChoice)

    # List Files In directory
    shList = []
    for file in os.listdir():
        if file.endswith(".sh"):
            shList.append(file)

    # Random Selection
    if len(shList) > 0:
        randomFile = os.getcwd() + os.path.sep + random.choice(shList)
        print("Your Randomly Selected Shell Script: " + randomFile)
        subprocess.call(randomFile)
    else:
        print("No Available Shell Scripts in This Directory")
else:
    print("Directory Does Not Exist")

sys.exit()
