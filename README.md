# UmaMusumeSmartReplacer Ver 3.0
## How To Use
1. Place all the scripts anywhere *(Recommanded to put them into one folder.)*
2. Double click the `UmaMusumeSmartReplace` file to open the UI
    - Alternatively, just run it in command line `>python UmaMusumeSmartReplace.py`

## Modes
### Manual
- Need `ID` and `Hash` of both File A and B. 
- For manually replacing a single file.
### Body
- Need `ID` of both File A and B. 
- Automatically replace one body.
### Head (Disabled by Default)
- Need `ID` of both File A and B. 
- *Currently does **not** work*
### Common (Disabled by Default)
- Need `ID` of both File A and B.
- Automatically replace every body type (ie. Height, Skin, etc).
- *Does **not** work for `1` & `3`*
- **May cause the game to not launch**
### Wetify (Disabled by Default)
- Need `ID` of File to *wet*.
- Automatically replace normal texture with wet version.
- Only tested on `4` and `5`
- Increase the texture file size by ~10x due to (lack of) compression
### External Restore
- Restore anything given `ID`, from external backup folder

## Notices
- If you are using Anaconda and double-click fails, download the [`sqlite.dll`](https://www.sqlite.org/download.html) and put it in `{UserName}\anaconda3\DLLs`
  - Alternatively, just run it in command line `>python UmaMusumeSmartReplace.py`
- The PATHs variables are automatically detected
- ***I am not responsible for whatever happens to your game/account***
- ***Modifying the game is against ToS***
- ***Highly recommanded to backup the whole `dat` folder before using***
