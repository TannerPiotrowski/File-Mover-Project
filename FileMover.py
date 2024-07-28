import os
import shutil

filesFrom = input("Enter the path of the folder you wish to have your files moved from: ")
filesTo = input("Enter the path of the folder you wish to move your files to: ")

files = os.listdir(filesFrom)
print(files)

for file in files:
    src_path = os.path.join(filesFrom, file)
    dest_path = os.path.join(filesTo, file)

    if os.path.exists(dest_path):
        print(f"File {file} already exists in the destination folder. Skipping.")
    else:
        shutil.move(src_path, dest_path)
        print(f"Moved {file} to {filesTo}")