import os
import winreg
import win32api

def read_reg(ep, p = r"", k = ''):
    try:
        key = winreg.OpenKeyEx(ep, p)
        value = winreg.QueryValueEx(key,k)
        if key:
            winreg.CloseKey(key)
        return value[0]
    except Exception as e:
        return None
    return None
def findsteampath():
    Path1 = "{}\\Microsoft\\Windows\\Start Menu\\Programs\\Steam\\Steam.lnk".format(os.getenv('APPDATA'))
    if os.path.exists(Path1):
        import sys
        import win32com.client 

        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(Path1)
        Path1Res = shortcut.Targetpath
    else:
        Path1Res = False
    Path2 = str(read_reg(ep = winreg.HKEY_LOCAL_MACHINE, p = r"SOFTWARE\Wow6432Node\Valve\Steam", k = 'InstallPath'))+r"\steam.exe"
    Path3 = str(read_reg(ep = winreg.HKEY_LOCAL_MACHINE, p = r"SOFTWARE\Valve\Steam", k = 'InstallPath'))+r"\steam.exe"
    if not os.path.exists(Path2):
        Path2 = None
    if not os.path.exists(Path3):
        Path3 = None
    PossiblePaths = [r"X:\Steam\steam.exe", r"X:\Program Files\Steam\steam.exe", r"X:\Program Files (x86)\Steam\steam.exe"]
    ValidHardPaths = []
    for Drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        Drive = Drive.replace(':\\', '')
        for path in PossiblePaths:
            path = path.replace("X", Drive)
            if os.path.exists(path):
                ValidHardPaths.append(path)
    if len(ValidHardPaths) == 0:
        ValidHardPaths = ["None"]
    #print("Registry64: " + str(Path2)+"|"+ "Registry32: "+ str(Path3)+"|"+ "Start Menu Shortcut: "+ str(Path1Res)+"|"+ "Possible Locations: " + ', '.join(ValidHardPaths)+"|")
    paths = [Path1Res, Path2, Path3, ValidHardPaths]
    print(paths)
    for path in paths:
        if path != "None" and path != False and path != None:
            steampath = str(path).replace("steam.exe", "").replace("['", "").replace("']", "")
            return(steampath)
    return("Steam.exe not found")