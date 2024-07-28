import os
import shutil

filesFrom = input("Enter the path of the folder you wish to have your files moved from: ")
filesTo = input("Enter the path of the folder you wish to move your files to: ")

files = os.listdir(filesFrom)
print(files)

# moves files from one folder to another
for file in files:
    srcPath = os.path.join(filesFrom, file)
    destPath = os.path.join(filesTo, file)

    if os.path.exists(destPath):
        print(f"File '{file}' already exists in the '{filesTo}' folder. Skipping.")
    else:
        shutil.move(srcPath, destPath)
        print(f"Moved '{file}' to '{filesTo}'")


# Organize the destination folder. sort by file type
# List all files in the destination folder
files = os.listdir(filesTo)

# Organize the destination folder by sorting files into subfolders based on file type
for file in files:
    filePath = os.path.join(filesTo, file)
    fileType = os.path.splitext(file)[1][1:]  # Extract file extension without the dot

    # If the file has no extension, consider it as 'misc'
    if not fileType:
        fileType = 'misc'

    typeFolder = os.path.join(filesTo, fileType)
    
    # Create the subfolder if it doesn't exist
    if not os.path.exists(typeFolder):
        os.makedirs(typeFolder)

    # Move the file into the respective subfolder
    shutil.move(filePath, os.path.join(typeFolder, file))
    print(f"Moved '{file}' to '{typeFolder}'")


    #print(len(fileType))