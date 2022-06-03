import common
import functions
import sharedfunctions
import os
import shutil
import tkinter as tk
import threading

# pfb, base, ctrl, diff, shade, mat
FILE_COUNT = 6

# 0 - 3
HEIGHT_RANGE = 4
# 0 - 2
SHAPE_RANGE = 3
# 0 - 4
BUST_RANGE = 5
# 0 - 3
SKIN_RANGE = 4

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

    if len(idA) != common.ID_LENGTH or len(idB) != common.ID_LENGTH:
        print('Invalid Inputs')
    else:
        for he in range(HEIGHT_RANGE):
            for sh in range(SHAPE_RANGE):
                for bu in range(BUST_RANGE):
                    for sk in range(SKIN_RANGE):
                        if idA[3] == '1':
                            A = sharedfunctions.getTrackHash(idA, he, sh, bu, sk, 1)
                        elif idA[3] == '3':
                            A = sharedfunctions.getSportsHash(idA, he, sh, bu, sk, 1)
                        else:
                            A = sharedfunctions.getCommonHash(idA, he, sh, bu, sk)

                        if idB[3] == '1':
                            B = sharedfunctions.getTrackHash(idB, he, sh, bu, sk, 2)
                        elif idB[3] == '3':
                            B = sharedfunctions.getSportsHash(idB, he, sh, bu, sk, 2)
                        else:
                            B = sharedfunctions.getCommonHash(idB, he, sh, bu, sk)

                        if A == -1 or B == -1:
                            continue

                        methods = []

                        for i in range(FILE_COUNT):
                            methods.append(threading.Thread(target = Replace, args = (A[i], B[i], idA, idB)))
                            methods[i].start()

                        for i in range(FILE_COUNT):
                            methods[i].join()

def onClear():
    oID.delete(0, 'end')
    nID.delete(0, 'end')
    print('Cleared Entry')

def run(mainWindow):
    global CURRENT_PATH
    global DATA_PATH
    global TEMP_PATH
    global oID
    global nID
    global editedFolder

    CURRENT_PATH = common.CURRENT_PATH
    DATA_PATH = common.DATA_PATH
    TEMP_PATH = common.TEMP_PATH

    editedFolder = TEMP_PATH + '/' + 'Edited'

    entries = tk.Frame(mainWindow, width = 600, height = 300, bg = "gray")
    buttons = tk.Frame(mainWindow, width = 600, height = 100, bg = "gray")

    entries.pack(fill = "both", expand = 1)
    buttons.pack(fill = "both",  expand = 1)

    tk.Label(entries, text="A -> B", fg = "white", bg = "black").pack(fill='both')

    tk.Label(entries, text="File A (to be replaced)", fg = "white", bg = "gray").pack()

    tk.Label(entries, text="ID: ", fg = "white", bg = "gray").pack()
    oID = tk.Entry(entries)
    oID.pack()

    tk.Label(entries, text="File B (the replacement)", fg = "white", bg = "gray").pack()

    tk.Label(entries, text="ID: ", fg = "white", bg = "gray").pack()
    nID = tk.Entry(entries)
    nID.pack()

    tk.Button(buttons, text = "Run", command = onRun, fg = "white", bg = "black", width = 10).pack(padx = 64, pady = 64,side = 'left', expand = 1, fill = 'both')
    tk.Button(buttons, text = "Clear", command = onClear, fg = "white", bg = "black", width = 10).pack(padx = 64, pady = 64,side = 'left', expand = 1, fill = 'both')