# UmaMusumeSmartReplacer
## How To Use
1. Place the 3 scripts anywhere *(Recommanded to put them into its own folder.)*
2. Double click the `UmaMusumeSmartReplace` file to open the UI
3. Enter the charater + outfit ID of file A and B *(`XXXX_YY`)*
4. The program will automatically create a backup of file A in the current folder
5. File A will then be replaced by file B with the correct edited IDs
- Clicking Restore will revert the changes (Requires File A's ID)

## Notices
- Currently only supports unique outfits. *(ie. Not Uniforms, etc)*
- If you are using Anaconda and double-click fails, download the [`sqlite.dll`](https://www.sqlite.org/download.html) and put it in `{UserName}\anaconda3\DLLs`
  - Alternatively, just run it in command line `>python UmaMusumeSmartReplace.py`
- The PATHs variables are automatically detected. No need to change them unless you also modify the `Initialize` part.
- ***I am not responsible for whatever happens to your game/account.***
- ***Modifying the game is against ToS***
