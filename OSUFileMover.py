# Avyah Sharma
# Automatically moves beatmaps 
# 12/3/2018

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
	cwd = os.getcwd()
	osu_dir = ""

	if cwd.replace("\\", "/").split("/")[1] == "Users":
		if os.path.exists("C:/Users/"+cwd.replace("\\", "/").split("/")[2]+"/AppData/Local/osu!"):
			osu_dir = "C:/Users/" + cwd.replace("\\", "/").split("/")[2] + "/AppData/Local/osu!"
			tarDir = osu_dir
			return tarDir

		if osu_dir == "":
			print("osu! song directory not found. Please input it manually.")
			osu_dir = input(":").replace("\\", "/").rstrip("/")
			tarDir = osu_dir
			return tarDir

srcDir = get_download_path()
tarDir = get_songs_path()

for file in os.listdir(srcDir):
    if file.endswith(".osz"):
        shutil.move(srcDir, tarDir)