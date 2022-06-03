import common
import functions
import os
import shutil
import tkinter as tk

def onRun():
    hashA = oHash.get()
    hashB = nHash.get()
    idA = oID.get()
    idB = nID.get()

    if len(hashA) == 0 or len(hashB) == 0 or len(idA) != common.ID_LENGTH or len(idB) != common.ID_LENGTH:
        print('Invalid Inputs')
    else:
        backupFolder = TEMP_PATH + '/' + 'BackUp'
        editedFolder = TEMP_PATH + '/' + 'Edited'

        folderA = hashA[0:2]
        fileA = DATA_PATH + '/' + folderA + '/' + hashA
        shutil.copy(fileA, backupFolder)

        folderB = hashB[0:2]
        fileB = DATA_PATH + '/' + folderB + '/' + hashB
        shutil.copyfile(fileB, editedFolder + '/' + hashA)

        new = editedFolder + '/' + hashA

        functions.replaceID(new, idB, idA)
        shutil.copyfile(new, fileA)

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
        folderA = hashA[0:2]

        edited = DATA_PATH + '/' + folderA + '/' + hashA
        backup = TEMP_PATH + '/' + 'BackUp' + '/' + hashA

        shutil.copyfile(backup, edited)

        print(f'File {hashA} has been restored from Backup!')

def run(mainWindow):
    global CURRENT_PATH
    global DATA_PATH
    global TEMP_PATH
    global oID
    global nID
    global oHash
    global nHash

    CURRENT_PATH = common.CURRENT_PATH
    DATA_PATH = common.DATA_PATH
    TEMP_PATH = common.TEMP_PATH

    operation = tk.Frame(mainWindow, width = 600, height = 30, bg = "gray")
    title1 = tk.Frame(mainWindow, width = 600, bg = "gray")
    title2 = tk.Frame(mainWindow, width = 600, bg = "gray")
    entry1 = tk.Frame(mainWindow, width = 600, bg = "gray")
    entry2 = tk.Frame(mainWindow, width = 600, bg = "gray")
    buttons = tk.Frame(mainWindow, width = 600, height = 100, bg = "gray")

    operation.pack(fill = "both", expand = 1)
    title1.pack(fill = "both", expand = 1)
    entry1.pack(fill = "both", expand = 1)
    title2.pack(pady = (30, 0),fill = "both", expand = 1)
    entry2.pack(fill = "both", expand = 1)
    buttons.pack(fill = "both", expand = 1)

    tk.Label(operation, text="A -> B", fg = "white", bg = "black").pack(fill='both')
    tk.Label(title1, text="File A (to be replaced)", fg = "white", bg = "gray").pack()
    tk.Label(title2, text="File B (the replacement)", fg = "white", bg = "gray").pack()
    
    e01_left = tk.Frame(entry1, width = 300, height = 60, bg = "gray")
    e01_left.pack(side = 'left', fill = "both", expand = 1)

    e01_right = tk.Frame(entry1, width = 300, height = 60, bg = "gray")
    e01_right.pack(side = 'left', fill = "both", expand = 1)

    tk.Label(e01_left, text="ID: ", fg = "white", bg = "gray").pack()
    oID = tk.Entry(e01_left)
    oID.pack()

    tk.Label(e01_right, text="Hash: ", fg = "white", bg = "gray").pack()
    oHash = tk.Entry(e01_right)
    oHash.pack()

    e02_left = tk.Frame(entry2, width = 200, height = 60, bg = "gray")
    e02_left.pack(side = 'left', fill = "both", expand = 1)

    e02_right = tk.Frame(entry2, width = 200, height = 60, bg = "gray")
    e02_right.pack(side = 'left', fill = "both", expand = 1)

    tk.Label(e02_left, text="ID: ", fg = "white", bg = "gray").pack()
    nID = tk.Entry(e02_left)
    nID.pack()

    tk.Label(e02_right, text="Hash: ", fg = "white", bg = "gray").pack()
    nHash = tk.Entry(e02_right)
    nHash.pack()

    tk.Button(buttons, text = "Run", command = onRun, fg = "white", bg = "black", width = 10).pack(padx = 32, pady = 32,side = 'left', expand = 1, fill = 'both')
    tk.Button(buttons, text = "Clear", command = onClear, fg = "white", bg = "black", width = 10).pack(padx = 32, pady = 32,side = 'left', expand = 1, fill = 'both')
    tk.Button(buttons, text = "Restore", command = onReset, fg = "white", bg = "black", width = 10).pack(padx = 32, pady = 32,side = 'left', expand = 1, fill = 'both')