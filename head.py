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
        pfbA_hash, matA_F_hash, matA_H_hash = functions.getHeadHash(idA)
        pfbB_hash, matB_F_hash, matB_H_hash = functions.getHeadHash(idB)

        backupFolder = TEMP_PATH + '/' + 'BackUp'
        editedFolder = TEMP_PATH + '/' + 'Edited'

        folderPA = pfbA_hash[0:2]
        file = DATA_PATH + '/' + folderPA + '/' + pfbA_hash
        shutil.copy(file, backupFolder)

        folderMA = matA_F_hash[0:2]
        file = DATA_PATH + '/' + folderMA + '/' + matA_F_hash
        shutil.copy(file, backupFolder)

        folderMA2 = matA_H_hash[0:2]
        file = DATA_PATH + '/' + folderMA2 + '/' + matA_H_hash
        shutil.copy(file, backupFolder)

        folderPB = pfbB_hash[0:2]
        file = DATA_PATH + '/' + folderPB + '/' + pfbB_hash
        shutil.copyfile(file, editedFolder + '/' + pfbA_hash)

        folderMB = matB_F_hash[0:2]
        file = DATA_PATH + '/' + folderMB + '/' + matB_F_hash
        shutil.copyfile(file, editedFolder + '/' + matA_F_hash)

        folderMB2 = matB_H_hash[0:2]
        file = DATA_PATH + '/' + folderMB2 + '/' + matB_H_hash
        shutil.copyfile(file, editedFolder + '/' + matA_H_hash)

        newPFB = editedFolder + '/' + pfbA_hash
        newMAT = editedFolder + '/' + matA_F_hash
        newMAT2 = editedFolder + '/' + matA_H_hash

        functions.replaceID(newPFB, idB, idA)
        functions.replaceID(newMAT, idB, idA)
        functions.replaceID(newMAT2, idB, idA)

        shutil.copyfile(newPFB, DATA_PATH + '/' + folderPA + '/' + pfbA_hash)
        shutil.copyfile(newMAT, DATA_PATH + '/' + folderMA + '/' + matA_F_hash)
        shutil.copyfile(newMAT2, DATA_PATH + '/' + folderMA2 + '/' + matA_H_hash)

        print(f'ID {idA} has been replaced by ID {idB}')

def onClear():
    oID.delete(0, 'end')
    nID.delete(0, 'end')
    print('Cleared Entry')

def onReset():
    idA = oID.get()
    pfbA_hash, matA_F_hash, matA_H_hash = functions.getHeadHash(idA)

    if len(idA) != common.ID_LENGTH:
        print('Invalid Inputs')
    else:
        tempFolder = TEMP_PATH + '/' + 'BackUp'

        folderA = pfbA_hash[0:2]

        edited = DATA_PATH + '/' + folderA + '/' + pfbA_hash
        backup = TEMP_PATH + '/' + 'BackUp' + '/' + pfbA_hash

        shutil.copyfile(backup, edited)

        folderB = matA_F_hash[0:2]

        edited = DATA_PATH + '/' + folderB + '/' + matA_F_hash
        backup = TEMP_PATH + '/' + 'BackUp' + '/' + matA_F_hash

        shutil.copyfile(backup, edited)

        folderC = matA_H_hash[0:2]

        edited = DATA_PATH + '/' + folderC + '/' + matA_H_hash
        backup = TEMP_PATH + '/' + 'BackUp' + '/' + matA_H_hash

        shutil.copyfile(backup, edited)

        print(f'ID {idA} has been restored from Backup!')

def run(mainWindow):
    global CURRENT_PATH
    global DATA_PATH
    global TEMP_PATH
    global oID
    global nID

    CURRENT_PATH = common.CURRENT_PATH
    DATA_PATH = common.DATA_PATH
    TEMP_PATH = common.TEMP_PATH

    entries = tk.Frame(mainWindow, width = 600, height = 300, bg = "gray")
    buttons = tk.Frame(mainWindow, width = 600, height = 100, bg = "gray")

    entries.pack(fill = "both", expand = 1)
    buttons.pack(fill = "both",  expand = 1)

    tk.Label(entries, text="A -> B", fg = "white", bg = "black").pack(fill='both')

    tk.Label(entries, text="File A (to be replaced)", fg = "white", bg = "gray").pack()

    tk.Label(entries, text="ID: ", fg = "white", bg = "gray").pack()
    oID = tk.Entry(entries)
    oID.pack()

    tk.Label(entries, text="File B (the replacement)", fg = "white", bg = "gray").pack(pady = (30, 0))

    tk.Label(entries, text="ID: ", fg = "white", bg = "gray").pack()
    nID = tk.Entry(entries)
    nID.pack()

    tk.Button(buttons, text = "Run", command = onRun, fg = "white", bg = "black", width = 10).pack(padx = 32, pady = 64,side = 'left', expand = 1, fill = 'both')
    tk.Button(buttons, text = "Clear", command = onClear, fg = "white", bg = "black", width = 10).pack(padx = 32, pady = 64,side = 'left', expand = 1, fill = 'both')
    tk.Button(buttons, text = "Restore", command = onReset, fg = "white", bg = "black", width = 10).pack(padx = 32, pady = 64,side = 'left', expand = 1, fill = 'both')