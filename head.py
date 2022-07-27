import common
import functions
import os
import shutil
import tkinter as tk
import threading

# pfb, cheek, eye, face, hair, mayu, tear
FILE_COUNT = 7

def Replace(hashA, hashB, idA, idB):
    folderA = hashA[0:2]
    fileA = DATA_PATH + '/' + folderA + '/' + hashA

    folderB = hashB[0:2]
    fileB = DATA_PATH + '/' + folderB + '/' + hashB
    shutil.copyfile(fileB, editedFolder + '/' + hashA)

    new = editedFolder + '/' + hashA

    functions.replaceID(new, idB, idA)
    shutil.copyfile(new, fileA)

def onRun():
    idA = oID.get()
    idB = nID.get()

    global  editedFolder

    if len(idA) != common.ID_LENGTH or len(idB) != common.ID_LENGTH:
        print('Invalid Inputs')
    else:
        A = functions.getHeadHash(idA)
        B = functions.getHeadHash(idB)

        editedFolder = TEMP_PATH + '/' + 'Edited'

        methods = []

        for i in range(FILE_COUNT):
            methods.append(threading.Thread(target = Replace, args = (A[i], B[i], idA, idB)))
            methods[i].start()

        for i in range(FILE_COUNT):
            methods[i].join()

        print(f'ID {idA} has been replaced by ID {idB}')

def onClear():
    oID.delete(0, 'end')
    nID.delete(0, 'end')
    print('Cleared Entry')

def onReset():
    """
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
        """
    print('Not Implemented!')


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