import common
import functions
import sharedfunctions
import os
import shutil
import tkinter as tk

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

def onClear():
    oID.delete(0, 'end')
    back.delete(0, 'end')
    print('Cleared Entry')

def onReset():
    BACKUP_PATH = back.get()
    idA = oID.get()

    if len(idA) != common.ID_LENGTH:
        print('Invalid Inputs')
    else:
        if idA[0] != '0':
            hashA = functions.getHash(idA)
            folderA = hashA[0:2]

            edited = DATA_PATH + '/' + folderA + '/' + hashA
            backup = BACKUP_PATH + '/' + folderA + '/' + hashA

            shutil.copyfile(backup, edited)
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

                            if A == -1:
                                continue

                            for i in range(FILE_COUNT):
                                hashA = A[i]
                                folderA = hashA[0:2]

                                edited = DATA_PATH + '/' + folderA + '/' + hashA
                                backup = BACKUP_PATH + '/' + folderA + '/' + hashA

                                shutil.copyfile(backup, edited)

def run(mainWindow):
    global CURRENT_PATH
    global DATA_PATH
    global TEMP_PATH
    global oID
    global back

    CURRENT_PATH = common.CURRENT_PATH
    DATA_PATH = common.DATA_PATH
    TEMP_PATH = common.TEMP_PATH

    entries = tk.Frame(mainWindow, width = 600, height = 300, bg = "gray")
    buttons = tk.Frame(mainWindow, width = 600, height = 100, bg = "gray")

    entries.pack(fill = "both", expand = 1)
    buttons.pack(fill = "both",  expand = 1)

    tk.Label(entries, text="External Restore", fg = "white", bg = "black").pack(fill='both')

    tk.Label(entries, text="ID: ", fg = "white", bg = "gray").pack()
    oID = tk.Entry(entries)
    oID.pack()

    tk.Label(entries, text="Path: ", fg = "white", bg = "gray").pack()
    back = tk.Entry(entries)
    back.pack()

    tk.Button(buttons, text = "Run", command = onReset, fg = "white", bg = "black", width = 10).pack(padx = 64, pady = 64,side = 'left', expand = 1, fill = 'both')
    tk.Button(buttons, text = "Clear", command = onClear, fg = "white", bg = "black", width = 10).pack(padx = 64, pady = 64,side = 'left', expand = 1, fill = 'both')