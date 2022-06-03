import common
import os
import pandas as pd

def getTrackHash(ID, height, shape, bust, skin, sex):
    prefab = f'3d/chara/body/bdy{ID}/pfb_bdy{ID}_0{sex}_{height}_{shape}_{bust}'
    base = f'3d/chara/body/bdy{ID}/textures/offline/tex_bdy{ID}_00_0_{bust}_00_base'
    ctrl = f'3d/chara/body/bdy{ID}/textures/offline/tex_bdy{ID}_00_0_{bust}_00_ctrl'
    diff = f'3d/chara/body/bdy{ID}/textures/offline/tex_bdy{ID}_00_{skin}_{bust}_00_diff'
    shade = f'3d/chara/body/bdy{ID}/textures/offline/tex_bdy{ID}_00_{skin}_{bust}_00_shad_c'
    mat = f'sourceresources/3d/chara/body/bdy{ID}/materials/mtl_bdy{ID}_0'

    p = pd.read_sql_query(f'select * from a where "n" = "{prefab}";', common.META)
    b = pd.read_sql_query(f'select * from a where "n" = "{base}";', common.META)
    c = pd.read_sql_query(f'select * from a where "n" = "{ctrl}";', common.META)
    d = pd.read_sql_query(f'select * from a where "n" = "{diff}";', common.META)
    s = pd.read_sql_query(f'select * from a where "n" = "{shade}";', common.META)
    m = pd.read_sql_query(f'select * from a where "n" = "{mat}";', common.META)

    if p.empty or d.empty or m.empty:
        return -1
    else:
        return [p.iloc[0,6], b.iloc[0,6], c.iloc[0,6], d.iloc[0,6], s.iloc[0,6], m.iloc[0,6]]

def getSportsHash(ID, height, shape, bust, skin, sex):
    prefab = f'3d/chara/body/bdy{ID}/pfb_bdy{ID}_0{sex}_{height}_{shape}_{bust}'
    base = f'3d/chara/body/bdy{ID}/textures/tex_bdy{ID}_00_0_{bust}_base'
    ctrl = f'3d/chara/body/bdy{ID}/textures/tex_bdy{ID}_00_0_{bust}_ctrl'
    diff = f'3d/chara/body/bdy{ID}/textures/tex_bdy{ID}_00_{skin}_{bust}_diff'
    shade = f'3d/chara/body/bdy{ID}/textures/tex_bdy{ID}_00_{skin}_{bust}_shad_c'
    mat = f'sourceresources/3d/chara/body/bdy{ID}/materials/mtl_bdy{ID}'

    p = pd.read_sql_query(f'select * from a where "n" = "{prefab}";', common.META)
    b = pd.read_sql_query(f'select * from a where "n" = "{base}";', common.META)
    c = pd.read_sql_query(f'select * from a where "n" = "{ctrl}";', common.META)
    d = pd.read_sql_query(f'select * from a where "n" = "{diff}";', common.META)
    s = pd.read_sql_query(f'select * from a where "n" = "{shade}";', common.META)
    m = pd.read_sql_query(f'select * from a where "n" = "{mat}";', common.META)

    if p.empty or d.empty or m.empty:
        return -1
    else:
        return [p.iloc[0,6], b.iloc[0,6], c.iloc[0,6], d.iloc[0,6], s.iloc[0,6], m.iloc[0,6]]

def getCommonHash(ID, height, shape, bust, skin):
    prefab = f'3d/chara/body/bdy{ID}/pfb_bdy{ID}_00_{height}_{shape}_{bust}'
    base = f'3d/chara/body/bdy{ID}/textures/tex_bdy{ID}_00_0_{bust}_base'
    ctrl = f'3d/chara/body/bdy{ID}/textures/tex_bdy{ID}_00_0_{bust}_ctrl'
    diff = f'3d/chara/body/bdy{ID}/textures/tex_bdy{ID}_00_{skin}_{bust}_diff'
    shade = f'3d/chara/body/bdy{ID}/textures/tex_bdy{ID}_00_{skin}_{bust}_shad_c'
    mat = f'sourceresources/3d/chara/body/bdy{ID}/materials/mtl_bdy{ID}'

    p = pd.read_sql_query(f'select * from a where "n" = "{prefab}";', common.META)
    b = pd.read_sql_query(f'select * from a where "n" = "{base}";', common.META)
    c = pd.read_sql_query(f'select * from a where "n" = "{ctrl}";', common.META)
    d = pd.read_sql_query(f'select * from a where "n" = "{diff}";', common.META)
    s = pd.read_sql_query(f'select * from a where "n" = "{shade}";', common.META)
    m = pd.read_sql_query(f'select * from a where "n" = "{mat}";', common.META)

    if p.empty or d.empty or m.empty:
        return -1
    else:
        return [p.iloc[0,6], b.iloc[0,6], c.iloc[0,6], d.iloc[0,6], s.iloc[0,6], m.iloc[0,6]]

def getWetHash(ID, skin, bust, wet = False):
    if not wet:
        base = f'3d/chara/body/bdy{ID}/textures/tex_bdy{ID}_00_0_{bust}_base'
        ctrl = f'3d/chara/body/bdy{ID}/textures/tex_bdy{ID}_00_0_{bust}_ctrl'
        diff = f'3d/chara/body/bdy{ID}/textures/tex_bdy{ID}_00_{skin}_{bust}_diff'
        shade = f'3d/chara/body/bdy{ID}/textures/tex_bdy{ID}_00_{skin}_{bust}_shad_c'
    else:
        base = f'3d/chara/body/bdy{ID}/textures/tex_bdy{ID}_00_0_{bust}_base_wet'
        ctrl = f'3d/chara/body/bdy{ID}/textures/tex_bdy{ID}_00_0_{bust}_ctrl_wet'
        diff = f'3d/chara/body/bdy{ID}/textures/tex_bdy{ID}_00_{skin}_{bust}_diff_wet'
        shade = f'3d/chara/body/bdy{ID}/textures/tex_bdy{ID}_00_{skin}_{bust}_shad_c_wet'

    b = pd.read_sql_query(f'select * from a where "n" = "{base}";', common.META)
    c = pd.read_sql_query(f'select * from a where "n" = "{ctrl}";', common.META)
    d = pd.read_sql_query(f'select * from a where "n" = "{diff}";', common.META)
    s = pd.read_sql_query(f'select * from a where "n" = "{shade}";', common.META)

    if d.empty:
        return -1
    else:
        return [b.iloc[0,6], c.iloc[0,6], d.iloc[0,6], s.iloc[0,6]]