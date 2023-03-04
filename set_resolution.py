from tkinter import *
from keyvalues import KeyValues
import os
from find_path import findsteampath
root = Tk()

newWidth = str(root.winfo_screenwidth())
newHeight = str(root.winfo_screenheight())

def replacelines(file, newWidth, newHeight):
    with open(file, 'r') as f1:
        lines = f1.readlines()

    with open(file, 'w') as f2:
        for line in lines:
            if "defaultres\"" in line:
                f2.write('	"setting.defaultres"		"' + newWidth + '"\n')
            elif "defaultresheight\"" in line:
                f2.write('	"setting.defaultresheight"		"' + newHeight + '"\n')
            else:
                f2.write(line)

def findgamefolder():
   libraryfolders = findsteampath()+"config\\libraryfolders.vdf"
   kv = KeyValues(filename=libraryfolders).dump().split("\n")

   paths = []
   for line in kv:
      if "path" in line:
         paths.append(line.split('"')[3]+"\\steamapps\\common\\Underlords")

   for path in paths:
      if os.path.exists(path):
         folder = path
   return folder

videosettings = findgamefolder()+"\\game\\dac\\cfg\\video.txt"
replacelines(videosettings, newWidth, newHeight)

os.system("D:\\SteamLibrary\\steamapps\\common\\Underlords\\game\\bin\\win64\\underlords.exe")
