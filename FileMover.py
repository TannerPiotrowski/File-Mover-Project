import os
import shutil

filesFrom = input("Enter the path of the folder you wish to have your files moved from: ")
filesTo = input("Enter the path of the folder you wish to move your files to: ")

files = os.listdir(filesFrom)
print(files)

for file in files:
    src_path = os.path.join(filesFrom, file)
    dest_path = os.path.join(filesTo, file)
    shutil.move(src_path, dest_path)