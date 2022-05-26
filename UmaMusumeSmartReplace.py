import os
import shutil
import tkinter as tk
import pandas as pd
import sqlite3

# Example:      McQueen wears Spe's Swimsuit
#   File A
#   McQueen (Anime)
#       ID:     1013_02
#   File B
#   Spe (Swimsuit)
#       ID:     1001_30

CURRENT_PATH = '{Folder of This File}'
DATA_PATH = '{UserName}/AppData/LocalLow/Cygames/umamusume/dat'
META = '{UserName}/AppData/LocalLow/Cygames/umamusume/meta'
TEMP_PATH = 'Replacer'

# XXXX_YY
ID_LENGTH = 7
# XXXX
ID_SHORT = 4

def replaceID(file, oldID, newID):
    l = os.path.getsize(file)

    with open(file, 'r+b') as FILE:
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

def getHash(ID):
    prefab = f'3d/chara/body/bdy{ID}/pfb_bdy{ID}'
    material = f'sourceresources/3d/chara/body/bdy{ID}/materials/mtl_bdy{ID}'

    pfb = pd.read_sql_query(f'select * from a where "n" = "{prefab}";', META)
    mat = pd.read_sql_query(f'select * from a where "n" = "{material}";', META)

    return pfb.iloc[0,6], mat.iloc[0,6]

def onRun():
    idA = oID.get()
    idB = nID.get()

    if len(idA) != ID_LENGTH or len(idB) != ID_LENGTH:
        print('Invalid Inputs')
    else:
        pfbA_hash, matA_hash = getHash(idA)
        pfbB_hash, matB_hash = getHash(idB)

        backupFolder = TEMP_PATH + '/' + 'BackUp'
        editedFolder = TEMP_PATH + '/' + 'Edited'

        folderPA = pfbA_hash[0:2]
        file = DATA_PATH + '/' + folderPA + '/' + pfbA_hash
        shutil.copy(file, backupFolder)

        folderMA = matA_hash[0:2]
        file = DATA_PATH + '/' + folderMA + '/' + matA_hash
        shutil.copy(file, backupFolder)

        folderPB = pfbB_hash[0:2]
        file = DATA_PATH + '/' + folderPB + '/' + pfbB_hash
        shutil.copyfile(file, editedFolder + '/' + pfbA_hash)

        folderMB = matB_hash[0:2]
        file = DATA_PATH + '/' + folderMB + '/' + matB_hash
        shutil.copyfile(file, editedFolder + '/' + matA_hash)

        newPFB = editedFolder + '/' + pfbA_hash
        newMAT = editedFolder + '/' + matA_hash

        replaceID(newPFB, idB, idA)
        replaceID(newMAT, idB, idA)

        shutil.copyfile(newPFB, DATA_PATH + '/' + folderPA + '/' + pfbA_hash)
        shutil.copyfile(newMAT, DATA_PATH + '/' + folderMA + '/' + matA_hash)

        print(f'ID {idA} has been replaced by ID {idB}')

def onClear():
    oID.delete(0, 'end')
    nID.delete(0, 'end')
    print('Cleared Entry')

def onReset():
    idA = oID.get()
    pfbA_hash, matA_hash = getHash(idA)

    if len(idA) != ID_LENGTH:
        print('Invalid Inputs')
    else:
        tempFolder = TEMP_PATH + '/' + 'BackUp'

        folderA = pfbA_hash[0:2]

        edited = DATA_PATH + '/' + folderA + '/' + pfbA_hash
        backup = TEMP_PATH + '/' + 'BackUp' + '/' + pfbA_hash

        shutil.copyfile(backup, edited)

        folderB = matA_hash[0:2]

        edited = DATA_PATH + '/' + folderB + '/' + matA_hash
        backup = TEMP_PATH + '/' + 'BackUp' + '/' + matA_hash

        shutil.copyfile(backup, edited)

        print(f'ID {idA} has been restored from Backup!')

# --- Initialize ---
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

roaming = os.getenv('APPDATA')
appdata = os.path.dirname(roaming)
DATA_PATH = appdata.replace(os.sep, '/') + '/LocalLow/Cygames/umamusume/dat'
META_PATH = appdata.replace(os.sep, '/') + '/LocalLow/Cygames/umamusume/meta'
print('Assets Folder Set to: ' + DATA_PATH)

META = sqlite3.connect(META_PATH)

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
mainWindow.geometry("225x175")
mainWindow.grid()

tk.Label(mainWindow, text="A -> B").grid(column=0, row=0, columnspan=3, sticky = tk.W + tk.E)

tk.Label(mainWindow, text="File A (to be replaced)").grid(column=0, row=1, columnspan=3, sticky = tk.W + tk.E)

tk.Label(mainWindow, text="ID: ").grid(column=0, row=2, sticky = tk.W)
oID = tk.Entry(mainWindow)
oID.grid(column=1, row=2, columnspan=2, sticky = tk.E)

tk.Label(mainWindow, text="File B (the replacement)").grid(column=0, row=3, columnspan=3, sticky = tk.W + tk.E)

tk.Label(mainWindow, text="ID: ").grid(column=0, row=4, sticky = tk.W)
nID = tk.Entry(mainWindow)
nID.grid(column=1, row=4, columnspan=2, sticky = tk.E)

tk.Button(mainWindow, text = "Run", command = onRun).grid(column=0, row=5)
tk.Button(mainWindow, text = "Clear", command = onClear).grid(column=1, row=5)
tk.Button(mainWindow, text = "Restore", command = onReset).grid(column=2, row=5)

mainWindow.mainloop()
