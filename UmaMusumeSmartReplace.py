import os
import shutil
import tkinter as tk

# Example:      McQueen wears Spe's Swimsuit
#   File A
#   McQueen (Anime)
#       ID:     1013_02
#       PFB:    SDB6WCQF25CCGGN55K64L7XUY2IHCTVM
#   File B
#   Spe (Swimsuit)
#       ID:     1001_30
#       PFB:    DIREYA4ULC3UD6AJY5WWAQR4IOHHOXAX

CURRENT_PATH = '{Folder of This File}'
DATA_PATH = '{UserName}/AppData/LocalLow/Cygames/umamusume/dat'
TEMP_PATH = 'Replacer'

# XXXX_YY
ID_LENGTH = 7
# XXXX
ID_SHORT = 4

def replaceID(oldFile, newFile, oldID, newID):
    l = os.path.getsize(oldFile)
    shutil.copyfile(oldFile, newFile)

    with open(newFile, 'r+b') as FILE:
        for i in range(l - ID_LENGTH):
            FILE.seek(i)
            byte = FILE.read(ID_LENGTH)

            if byte == str.encode(oldID):
                FILE.seek(i)
                FILE.write(str.encode(newID))

        for i in range(l - ID_SHORT):
            FILE.seek(i)
            byte = FILE.read(ID_SHORT)

            if byte == str.encode(oldID[0:4]):
                FILE.seek(i)
                FILE.write(str.encode(newID[0:4]))

    FILE.close()

def onRun():
    hashA = oHash.get()
    hashB = nHash.get()
    idA = oID.get()
    idB = nID.get()

    if len(hashA) == 0 or len(hashB) == 0 or len(idA) != ID_LENGTH or len(idB) != ID_LENGTH:
        print('Invalid Inputs')
    else:
        tempFolder = TEMP_PATH + '/' + 'BackUp'

        folderA = hashA[0:2]
        fileA = DATA_PATH + '/' + folderA + '/' + hashA
        shutil.copy(fileA, tempFolder)

        folderB = hashB[0:2]
        fileB = DATA_PATH + '/' + folderB + '/' + hashB
        shutil.copy(fileB, tempFolder)

        replacement = TEMP_PATH + '/' + 'BackUp' + '/' + hashB
        edited = TEMP_PATH + '/' + 'Edited' + '/' + hashA

        replaceID(replacement, edited, idB, idA)
        shutil.copyfile(edited, fileA)

        print(f'File {hashA} has been replaced by {hashB}')

def onClear():
    oID.delete(0, 'end')
    oHash.delete(0, 'end')
    nID.delete(0, 'end')
    nHash.delete(0, 'end')
    print('Cleared Entry')

def onReset():
    hashA = oHash.get()

    if len(hashA) == 0:
        print('Invalid Inputs')
    else:
        tempFolder = TEMP_PATH + '/' + 'BackUp'

        folderA = hashA[0:2]

        edited = DATA_PATH + '/' + folderA + '/' + hashA
        backup = TEMP_PATH + '/' + 'BackUp' + '/' + hashA

        shutil.copyfile(backup, edited)

        print(f'File {hashA} has been restored from Backup!')

# --- Initialize ---
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

roaming = os.getenv('APPDATA')
appdata = os.path.dirname(roaming)
DATA_PATH = appdata.replace(os.sep, '/') + '/LocalLow/Cygames/umamusume/dat'
print('Assets Folder Set to: ' + DATA_PATH)
    
if not os.path.exists(TEMP_PATH):
    os.mkdir(TEMP_PATH)

if not os.path.exists(os.path.join(TEMP_PATH, 'BackUp')):
    os.mkdir(os.path.join(TEMP_PATH, 'BackUp'))

if not os.path.exists(os.path.join(TEMP_PATH, 'Edited')):
    os.mkdir(os.path.join(TEMP_PATH, 'Edited'))

TEMP_PATH = (os.path.join(CURRENT_PATH, TEMP_PATH)).replace(os.sep, '/')
print('Temp Folder Set to: ' + TEMP_PATH)
    
# --- Main ---
mainWindow = tk.Tk()
mainWindow.title('Replacer')
mainWindow.geometry("240x240")
mainWindow.grid()

tk.Label(mainWindow, text="A -> B").grid(column=0, row=0, columnspan=3, sticky = tk.W + tk.E)

tk.Label(mainWindow, text="File A (to be replaced)").grid(column=0, row=1, columnspan=3, sticky = tk.W + tk.E)

tk.Label(mainWindow, text="ID: ").grid(column=0, row=2, sticky = tk.W)
oID = tk.Entry(mainWindow, width = 20)
oID.grid(column=1, row=2, columnspan=2, sticky = tk.E)

tk.Label(mainWindow, text="Hash: ").grid(column=0, row=3, sticky = tk.W)
oHash = tk.Entry(mainWindow, width = 20)
oHash.grid(column=1, row=3, columnspan=2, sticky = tk.E)

tk.Label(mainWindow, text="File B (the replacement)").grid(column=0, row=4, columnspan=3, sticky = tk.W + tk.E)

tk.Label(mainWindow, text="ID: ").grid(column=0, row=5, sticky = tk.W)
nID = tk.Entry(mainWindow, width = 20)
nID.grid(column=1, row=5, columnspan=2, sticky = tk.E)

tk.Label(mainWindow, text="Hash: ").grid(column=0, row=6, sticky = tk.W)
nHash = tk.Entry(mainWindow, width = 20)
nHash.grid(column=1, row=6, columnspan=2, sticky = tk.E)

tk.Button(mainWindow, text = "Run", command = onRun).grid(column=0, row=7)
tk.Button(mainWindow, text = "Clear", command = onClear).grid(column=1, row=7)
tk.Button(mainWindow, text = "Restore", command = onReset).grid(column=2, row=7)

mainWindow.mainloop()