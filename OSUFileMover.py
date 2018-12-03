# Avyah Sharma
# Automatically moves beatmaps 

import shutil
import os

def get_download_path():
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')

def get_songs_path():
    tarDir = os.path.abspath("osu!.exe")
    tarDir.replace("osu!.exe", "Songs")
    return tarDir

srcDir = get_download_path()
tarDir = get_songs_path()

for file in os.listdir(srcDir):
    if file.endswith(".osz"):
        shutil.move(srcDir, tarDir)

