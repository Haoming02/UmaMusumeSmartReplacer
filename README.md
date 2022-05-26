# UmaMusumeSmartReplacer
## How To Use
1. Place the script anywhere *(Recommanded to put it into its own folder.)*
2. Double click the script to open the UI
3. Enter the charater + outfit ID of file A and B *(`XXXX_YY`)*
4. The program will automatically create a backup of file A in the current folder
5. File A will then be replaced by file B with the correct edited IDs
- Clicking Restore will revert the changes (Requires File A's ID)

## Notices
- An example is given in the file.
- Currently does **not** support shared outfits. (eg. Uniforms)
- The PATHs variables are automatically detected. No need to change them unless you also modify the `Initialize` part.
- If you are using Anaconda and double-click fails, download the [`sqlite.dll`](https://www.sqlite.org/download.html) and put it in `{UserName}\anaconda3\DLLs`
  - Alternatively, just run it in command line `>python UmaMusumeSmartReplace.py`
- ***I am not responsible for whatever happens to your game.***
