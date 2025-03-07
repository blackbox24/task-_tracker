import json
import sys
import os
from datetime import datetime


# check if directory exists
BASE_DIR = os.getcwd()
DATA_DIR = f"{BASE_DIR}\\..\\data"
DATA_DIR_FILE = f"{BASE_DIR}\\..\\data\\data.json"
ROOT_DIR = f"{BASE_DIR}\\..\\"
ID = 0

ACTIONS = ["add","update","delete","list"," mark-in-progress","mark-done"]


def fileIsEmpty():
    try:
        with open(DATA_DIR_FILE,"r") as f:
            file = json.loads(f.read())
            return False
    except:
        return True

def generateID():
    if not fileIsEmpty():
        with open(DATA_DIR_FILE,"r") as f:
            file = json.loads(f.read())
            return len(file)
        
    return 0

def addData():
    # isempty
    ID = generateID()
    
    if fileIsEmpty():
        with open(DATA_DIR_FILE,"w+") as f:
            data = [
                {
                    "id": ID,
                    "description": sys.argv[2],
                    "status": "todo",
                    "createdAt":str(datetime.now()),
                    "updatedAt":str(datetime.now()),
                }
            ]
            file = json.dump(data,f)
    else:
        with open(DATA_DIR_FILE,"r+") as f:
            prev_data = json.loads(f.read())
            new_data = {
                "id": ID,
                "description": sys.argv[2],
                "status": "todo",
                "createdAt":str(datetime.now()),
                "updatedAt":str(datetime.now())
            }
            f.seek(0)
            f.truncate()
            prev_data.append(new_data)
            json.dump(prev_data,f)
            print("Task added successfully (ID: %i)" %ID)
    return 0

def updateData():
    index = int(sys.argv[2])
    if not fileIsEmpty():
        with open(DATA_DIR_FILE,"r+") as f:
            file = json.loads(f.read())
            for i in range(len(file)):

                if file[i]["id"] == index:
                    file[i]["description"] = sys.argv[3]
                    file[i]["updatedAt"] = str(datetime.now())
                    f.seek(0)
                    f.truncate()
                    json.dump(file,f)
                    print("Update complete")
                    break

                elif file[i]["id"] != sys.argv[2] and i == len(file) -1:
                    print("index cannot be found")
                    
    else:
        print("File is empty")
    return 0

def listData():
    try:
        with open(DATA_DIR_FILE,"r+") as f:
            file = json.loads(f.read())
            for i in file:
                    print(i)
    except:
        print("File is empty")

    return 0
if not os.path.isdir(DATA_DIR):
    os.chdir(ROOT_DIR)
    os.mkdir(DATA_DIR)

# files exists
files = os.listdir(DATA_DIR)

if not "data.json" in files:
    file = open(DATA_DIR+"\\data.json",mode="w")
    file.write("{}")
    file.close()

# make sure actions args is in ACTIONS list
if sys.argv[1] in ACTIONS:
    action = sys.argv[1]
    if action == "add" and len(sys.argv) == 3:
        output = addData()

    elif action  == "update" and len(sys.argv) == 4:
       output = updateData()
    
    elif action  == "delete" and len(sys.argv) == 3:
        
        try:
            index = int(sys.argv[2])
            with open(DATA_DIR_FILE,"r+") as f:
                # id exists
                file = json.loads(f.read())
                for i in range(len(file)):
                    if file[i]["id"] == sys.argv[2]:
                        pass
        except:
            print("File is empty")

    elif action  == "list":
        output = listData()

    elif action  == "mark-in-progress":
        updateData()
    
    elif action  == "mark-done":
        updateData()

else:
    print("Invalid command")
    # if sys.argv[1]  ==  "add" and sys.argv[2] != None:
    #     # check the next args to be a string
    #     with open(DATA_DIR_FILE,mode="w+") as f:
    #         data = {"id":1,"description":sys.argv[2],"status":"todo","createdAt":str(datetime.now()),"updatedAt":str(datetime.now())}
    #         json.dump(data,f)