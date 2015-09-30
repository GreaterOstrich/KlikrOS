# Random.py
import os
import shutil

def update():
	for i in os.listdir("files"):
		os.remove("files/"+i)

	for x in os.listdir("newfiles"):
		shutil.copy2("newfiles/"+x, "files/"+x)

def downloadUpdate():
	print("pretending to download update")

def getCurrentInfo():
	with open("info.txt") as f:
		content = f.readlines()[0]
		info = {}
		for i in content.split(","):
			info[i.split("=")[0]] = [i.split("=")[1]] 
	return info

print("Checking for updates")
print("Simulate downloaded updates")
print("Update starting...")
update()
print("Updated complete")

print(getCurrentInfo()["SerialID"])