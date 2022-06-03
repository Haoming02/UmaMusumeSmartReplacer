import common
import functions
import sharedfunctions
import os
import shutil
import tkinter as tk
import UnityPy
import sys
from PIL import Image

# Base ; Ctrl ; Diff ; Shade
FILE_COUNT = 4
TEMP_PATH = "TEMP"

# 0 - 3
SKIN_RANGE = 4
# 0 - 4
BUST_RANGE = 5

def unpackAssets(file):
    env = UnityPy.load(file)
    for obj in env.objects:
        if obj.type.name =="Texture2D":
            data = obj.read()
            dest = os.path.join(TEMP_PATH, data.name)

            dest, temp = os.path.splitext(dest)
            out = dest[:-4] + ".tga"

            img = data.image
            img.save(out)

def replaceAssets(file):
    env = UnityPy.load(file)

    for obj in env.objects:
        if obj.type.name == "Texture2D":
            objData = obj.read()
            pil_img = Image.open(TEMP_PATH + '/' + objData.name + '.tga')
            objData.set_image(img = pil_img, in_cab = False)
            objData.save()
    
    with open(file[:-4], "wb+") as f:
        f.write(env.file.save())

def replaceTexture(normal, wet):
    unpackAssets(wet)
    replaceAssets(normal)

def onRun():
    if not os.path.exists(TEMP_PATH):
        os.mkdir(TEMP_PATH)
    idA = oID.get()

    if len(idA) != common.ID_LENGTH:
        print('Invalid Inputs')
    else:
        for sk in range(SKIN_RANGE):
            for bu in range(BUST_RANGE):
                A = sharedfunctions.getWetHash(idA, sk, bu)
                B = sharedfunctions.getWetHash(idA, sk, bu, True)

                if A == -1 or B == -1:
                    continue

                for i in range(FILE_COUNT):
                    hashA = A[i]
                    hashB = B[i]

                    folderA = hashA[0:2]
                    fileA = DATA_PATH + '/' + folderA + '/' + hashA

                    folderB = hashB[0:2]
                    fileB = DATA_PATH + '/' + folderB + '/' + hashB

                    shutil.copyfile(fileA, TEMP_PATH + '/' + hashA + '_old')
                    shutil.copy(fileB, TEMP_PATH)

                    normal = TEMP_PATH + '/' + hashA + '_old'
                    wet = TEMP_PATH + '/' + hashB

                    replaceTexture(normal, wet)
                    shutil.copyfile(TEMP_PATH + '/' + hashA, fileA)
    shutil.rmtree(TEMP_PATH)

def onRestore():
    BACKUP_PATH = back.get()
    idA = oID.get()

    if len(idA) != common.ID_LENGTH:
        print('Invalid Inputs')
    else:
        for sk in range(SKIN_RANGE):
            for bu in range(BUST_RANGE):
                A = sharedfunctions.getWetHash(idA, sk, bu)

                if A == -1:
                    continue

                for i in range(FILE_COUNT):
                    hashA = A[i]

                    folderA = hashA[0:2]
                    fileA = BACKUP_PATH + '/' + folderA + '/' + hashA
                    fileB = DATA_PATH + '/' + folderA + '/' + hashA

                    shutil.copyfile(fileA, fileB)

def onClear():
    oID.delete(0, 'end')
    print('Cleared Entry')

def run(mainWindow):
    global CURRENT_PATH
    global DATA_PATH
    global oID
    global back

    CURRENT_PATH = common.CURRENT_PATH
    DATA_PATH = common.DATA_PATH

    entries = tk.Frame(mainWindow, width = 600, height = 300, bg = "gray")
    buttons = tk.Frame(mainWindow, width = 600, height = 100, bg = "gray")

    entries.pack(fill = "both", expand = 1)
    buttons.pack(fill = "both",  expand = 1)

    tk.Label(entries, text="A -> Wet", fg = "white", bg = "black").pack(fill='both')

    tk.Label(entries, text="File A (to be wet)", fg = "white", bg = "gray").pack()

    tk.Label(entries, text="ID: ", fg = "white", bg = "gray").pack()
    oID = tk.Entry(entries)
    oID.pack()

    tk.Label(entries, text="Path: ", fg = "white", bg = "gray").pack()
    back = tk.Entry(entries)
    back.pack()

    tk.Button(buttons, text = "Run", command = onRun, fg = "white", bg = "black", width = 10).pack(padx = 64, pady = 64,side = 'left', expand = 1, fill = 'both')
    tk.Button(buttons, text = "Restore", command = onRestore, fg = "white", bg = "black", width = 10).pack(padx = 64, pady = 64,side = 'left', expand = 1, fill = 'both')
    tk.Button(buttons, text = "Clear", command = onClear, fg = "white", bg = "black", width = 10).pack(padx = 64, pady = 64,side = 'left', expand = 1, fill = 'both')