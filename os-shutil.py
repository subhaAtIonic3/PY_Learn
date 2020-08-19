import os
import shutil
import send2trash

#  pwd
#  /Volumes/WD_ELEMENTS/python/Learn_Python/learn

f = open("practice.txt", "w+")
f.write("This is some test text")
f.close()

print(os.getcwd())
# print(os.listdir())

print(os.listdir("/Volumes"))

shutil.move("practice.txt",
            "/Volumes/WD_ELEMENTS/python/Learn_Python/learn/dummy_folder")

shutil.move(
    "/Volumes/WD_ELEMENTS/python/Learn_Python/learn/dummy_folder/practice.txt", os.getcwd())

send2trash.send2trash("practice.txt")

for folder, sub_folders, files in os.walk("MyMainPackage"):
    print("Currently looking at folder: " + folder)
    for f in files:
        print("files are =>", f)
    for sub_folder in sub_folders:
        print("sub folder is =>", sub_folder)
