# Random.py
import os
import shutil

def update():
	for i in os.listdir("files"):
		os.remove("files/"+i)

	for x in os.listdir("newfiles"):
		shutil.copy2("newfiles/"+x, "files/"+x)

print("Checking for updates")
print("Simulate downloaded updates")
print("Update starting...")
update()
print("Updated complete")

