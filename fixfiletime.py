import pywintypes
import win32con
import win32file
import os
import time


def changeFileCreationTime(fname, creationtime, modifytime):
    winctime = pywintypes.Time(creationtime)
    winmtime = pywintypes.Time(modifytime)
    winfile = win32file.CreateFile(
        fname, win32con.GENERIC_WRITE,
        win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
        None, win32con.OPEN_EXISTING,
        win32con.FILE_ATTRIBUTE_NORMAL, None)

    win32file.SetFileTime(winfile, winctime, None, winmtime)

    winfile.close()

def main():
    file_name = "K:\\Work\\youdaonote-pull\\test.txt"
    ctime = os.path.getctime(file_name)
    mtime = os.path.getmtime(file_name)
    newctime = time.mktime((2009,2,17,17,3,38,1,48,0))
    newmtime = time.mktime((2010,3,17,17,3,38,1,48,0))
    changeFileCreationTime(file_name, newctime, newmtime)

if __name__ == '__main__':
    main()
