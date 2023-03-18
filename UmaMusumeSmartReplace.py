import common
import manual
import body
import shared
#import wetify
import exres
import tkinter as tk
from tkinter import ttk

def main():
	root = tk.Tk()
	root.title('Uma Musume Smart Replacer')
	root.geometry("600x400")

	mainWindow = ttk.Notebook(root)
	mainWindow.pack(fill = "both", expand = 1)

	manualTab = tk.Frame(mainWindow, width = 600, height = 400, bg = "gray")
	bodyTab = tk.Frame(mainWindow, width = 600, height = 400, bg = "gray")
	commonTab = tk.Frame(mainWindow, width = 600, height = 400, bg = "gray")
	#wetTab = tk.Frame(mainWindow, width = 600, height = 400, bg = "gray")
	externalTab = tk.Frame(mainWindow, width = 600, height = 400, bg = "gray")

	manualTab.pack(fill = "both", expand = 1)
	bodyTab.pack(fill = "both", expand = 1)
	commonTab.pack(fill = "both", expand = 1)
	#wetTab.pack(fill = "both", expand = 1)
	externalTab.pack(fill = "both", expand = 1)

	mainWindow.add(manualTab, text="Manual")
	mainWindow.add(bodyTab, text="Body")
	mainWindow.add(commonTab, text="Common")
	#mainWindow.add(wetTab, text="Wet-ify")
	mainWindow.add(externalTab, text="External Restore")

	manual.run(manualTab)
	body.run(bodyTab)
	shared.run(commonTab)		# Extremely Buggy
	#wetify.run(wetTab)			# Only tested for 4 & 5
	exres.run(externalTab)

	root.mainloop()

if __name__ == '__main__':
	common.initialize()
	main()