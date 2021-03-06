import common
import os
import pandas as pd

def replaceID(file, oldID, newID):
    l = os.path.getsize(file)

    with open(file, 'r+b') as FILE:
        for i in range(l - common.ID_LENGTH):
            FILE.seek(i)
            byte = FILE.read(common.ID_LENGTH)

            if byte == str.encode(oldID):
                FILE.seek(i)
                FILE.write(str.encode(newID))

        for i in range(l - common.ID_SHORT):
            FILE.seek(i)
            byte = FILE.read(common.ID_SHORT)

            if byte == str.encode(oldID[0:4]):
                FILE.seek(i)
                FILE.write(str.encode(newID[0:4]))

    FILE.close()

def getHeadHash(ID):
    prefab = f'3d/chara/head/chr{ID}/pfb_chr{ID}'
    cheek = f'sourceresources/3d/chara/head/chr{ID}/materials/mtl_chr{ID}_cheek'
    eye = f'sourceresources/3d/chara/head/chr{ID}/materials/mtl_chr{ID}_eye'
    face = f'sourceresources/3d/chara/head/chr{ID}/materials/mtl_chr{ID}_face'
    hair = f'sourceresources/3d/chara/head/chr{ID}/materials/mtl_chr{ID}_hair'
    mayu = f'sourceresources/3d/chara/head/chr{ID}/materials/mtl_chr{ID}_mayu'
    tear = f'sourceresources/3d/chara/head/chr{ID}/materials/mtl_chr{ID}_tear'

    p = pd.read_sql_query(f'select * from a where "n" = "{prefab}";', common.META)
    c = pd.read_sql_query(f'select * from a where "n" = "{cheek}";', common.META)
    e = pd.read_sql_query(f'select * from a where "n" = "{eye}";', common.META)
    f = pd.read_sql_query(f'select * from a where "n" = "{face}";', common.META)
    h = pd.read_sql_query(f'select * from a where "n" = "{hair}";', common.META)
    m = pd.read_sql_query(f'select * from a where "n" = "{mayu}";', common.META)
    t = pd.read_sql_query(f'select * from a where "n" = "{tear}";', common.META)

    return [p.iloc[0,6], c.iloc[0,6], e.iloc[0,6], f.iloc[0,6], h.iloc[0,6], m.iloc[0,6], t.iloc[0,6]]

def getHash(ID):
    prefab = f'3d/chara/body/bdy{ID}/pfb_bdy{ID}'
    material = f'sourceresources/3d/chara/body/bdy{ID}/materials/mtl_bdy{ID}'

    pfb = pd.read_sql_query(f'select * from a where "n" = "{prefab}";', common.META)
    mat = pd.read_sql_query(f'select * from a where "n" = "{material}";', common.META)
    return pfb.iloc[0,6], mat.iloc[0,6]