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
HELP = """
HELP DOCS 
COMMAND [ACTION ] [INDEX] [OPTION]

# Adding a new task
task-cli add "Buy groceries"
# Output: Task added successfully (ID: 1)

# Updating and deleting tasks
task-cli update 1 "Buy groceries and cook dinner"
task-cli delete 1

# Marking a task as in progress or done
task-cli mark-in-progress 1
task-cli mark-done 1

# Listing all tasks
task-cli list

# Listing tasks by status
task-cli list done
task-cli list todo
task-cli list in-progress
"""
ACTIONS = ["add","update","delete","list","mark-in-progress","mark-done"]
print(BASE_DIR)

def fileIsEmpty():
    try:
        with open(DATA_DIR_FILE,"r") as f:
            file = json.loads(f.read())
            return False
    except json.decoder.JSONDecodeError as e:
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
            print("Task added successfully (ID: %i)" %ID)
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
    except json.decoder.JSONDecodeError as e:
        print("File is empty")

    return 0

def deleteData():
    try:
        index = int(sys.argv[2])
        with open(DATA_DIR_FILE,"r+") as f:
            # id exists
            file = json.loads(f.read())
            for i in range(len(file)):
                if file[i]["id"] == index:
                    file.remove(file[i])
                    f.seek(0)
                    f.truncate()
                    json.dump(file,f)
                    break
                elif file[i]["id"] != index and i == len(file) -1:
                    print("Index cannot be found")
                    
    except ValueError:
        print("Invalid index")

    except json.decoder.JSONDecodeError as e:
        print("File is empty")
    
    return 0

def markInProgress():
    try:
        index = int(sys.argv[2])
        with open(DATA_DIR_FILE,"r+") as f:
            file = json.loads(f.read())
            for i in range(len(file)):
                if file[i]["id"] == index:
                    file[i]["status"] = "in-progress"
                    f.seek(0)
                    f.truncate()
                    json.dump(file,f)
                    print("Task %i marked as in-progress" %file[i]["id"])
                    break

                elif file[i]["id"] != index and i == len(file) - 1:
                    print("Index cannot be found")

    except ValueError as e:
        print("Invalid index ",e)
    
    except json.decoder.JSONDecodeError as e:
        print("File is empty")
    return 0

def markDone():
    try:
        index = int(sys.argv[2])
        with open(DATA_DIR_FILE,"r+") as f:
            file = json.loads(f.read())
            for i in range(len(file)):
                if file[i]["id"] == index:
                    file[i]["status"] = "done"
                    f.seek(0)
                    f.truncate()
                    json.dump(file,f)
                    print("Task %i marked as done" %file[i]["id"])
                    break

                elif file[i]["id"] != index and i == len(file) - 1:
                    print("Index cannot be found")

    except ValueError as e:
        print("Invalid index ",e)
    
    except json.decoder.JSONDecodeError as e:
        print("File is empty")
    return 0


def fileStatus():
    try:
        with open(DATA_DIR_FILE,"r+") as f:
            file = json.loads(f.read())
            ids = 0
            for i in range(len(file)):
                if file[i]["status"] == sys.argv[2]:
                    print(file[i])
                    ids += 1
                elif file[i]["status"] != sys.argv[2] and i == len(file) - 1 and ids <= 0:
                    print("%s Status cannot be found"  %sys.argv[2])
                        
    except json.decoder.JSONDecodeError as e:
        print("File is empty\n",e)

if not os.path.isdir(DATA_DIR):
    os.chdir(ROOT_DIR)
    os.mkdir(DATA_DIR)

# files exists
files = os.listdir(DATA_DIR)

if not "data.json" in files:
    file = open(DATA_DIR+"\\data.json",mode="w")
    file.close()

# make sure actions args is in ACTIONS list
try:
    if sys.argv[1] in ACTIONS:
        action = sys.argv[1]
        if action == "add" and len(sys.argv) == 3:
            output = addData()

        elif action  == "update" and len(sys.argv) == 4:
            output = updateData()
        
        elif action  == "delete" and len(sys.argv) == 3:
            output = deleteData()

        elif action  == "list":
            if len(sys.argv) == 2:
                output = listData()
            elif len(sys.argv) == 3:
                output = fileStatus()


        # print("....")

        elif action  == "mark-in-progress" and len(sys.argv) == 3:
            output = markInProgress()
                    
        elif action  == "mark-done":
            output = markDone()

    else:
        print(HELP)
except:
    print(HELP)
    # if sys.argv[1]  ==  "add" and sys.argv[2] != None:
    #     # check the next args to be a string
    #     with open(DATA_DIR_FILE,mode="w+") as f:
    #         data = {"id":1,"description":sys.argv[2],"status":"todo","createdAt":str(datetime.now()),"updatedAt":str(datetime.now())}
    #         json.dump(data,f)