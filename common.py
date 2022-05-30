import os
import sqlite3

# XXXX_YY
ID_LENGTH = 7
# XXXX
ID_SHORT = 4

def initialize():
    global CURRENT_PATH
    global DATA_PATH
    global META
    global TEMP_PATH

    CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))

    roaming = os.getenv('APPDATA')
    appdata = os.path.dirname(roaming)

    DATA_PATH = appdata.replace(os.sep, '/') + '/LocalLow/Cygames/umamusume/dat'
    print('Assets Folder Set to: ' + DATA_PATH)

    META_PATH = appdata.replace(os.sep, '/') + '/LocalLow/Cygames/umamusume/meta'
    META = sqlite3.connect(META_PATH)

    TEMP_PATH = 'Replacer'
    if not os.path.exists(TEMP_PATH):
        os.mkdir(TEMP_PATH)

    if not os.path.exists(os.path.join(TEMP_PATH, 'BackUp')):
        os.mkdir(os.path.join(TEMP_PATH, 'BackUp'))

    if not os.path.exists(os.path.join(TEMP_PATH, 'Edited')):
        os.mkdir(os.path.join(TEMP_PATH, 'Edited'))

    TEMP_PATH = (os.path.join(CURRENT_PATH, TEMP_PATH)).replace(os.sep, '/')
    print('Temp Folder Set to: ' + TEMP_PATH)