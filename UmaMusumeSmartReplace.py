import common
import functions
import os
import shutil
import tkinter as tk

def onRun():
    idA = oID.get()
    idB = nID.get()

    if len(idA) != common.ID_LENGTH or len(idB) != common.ID_LENGTH:
        print('Invalid Inputs')
    else:
        pfbA_hash, matA_hash = functions.getHash(idA)
        pfbB_hash, matB_hash = functions.getHash(idB)

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

        functions.replaceID(newPFB, idB, idA)
        functions.replaceID(newMAT, idB, idA)

        shutil.copyfile(newPFB, DATA_PATH + '/' + folderPA + '/' + pfbA_hash)
        shutil.copyfile(newMAT, DATA_PATH + '/' + folderMA + '/' + matA_hash)

        print(f'ID {idA} has been replaced by ID {idB}')

def onClear():
    oID.delete(0, 'end')
    nID.delete(0, 'end')
    print('Cleared Entry')

def onReset():
    idA = oID.get()
    pfbA_hash, matA_hash = functions.getHash(idA)

    if len(idA) != common.ID_LENGTH:
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

# --- Main ---
common.initialize()

global CURRENT_PATH
global DATA_PATH
global TEMP_PATH

CURRENT_PATH = common.CURRENT_PATH
DATA_PATH = common.DATA_PATH
TEMP_PATH = common.TEMP_PATH

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