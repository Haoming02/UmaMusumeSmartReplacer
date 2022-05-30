import common
import os
import pandas as pd

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