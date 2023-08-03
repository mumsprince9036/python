import os
import pathlib
import zipfile
import sys

dirName=input("enter directory that you want to backup")
if not os.path.isdir(dirName):
    print("directory",dirName,"doesnt exist")
    sys.exit(0)

curDiretory = pathlib.Path(dirName)

with zipfile.ZipFile("myZip.zip",mode="w")as archive:
    for file_path in curDiretory.rglob("*"):
       archive.write(file_path,arcname=file_path.relative_to(curDiretory))

if os.path.isfile("myZip.zip"):
    print("Archive","myZipzip","created successfully")
else:
    print("error creating zip archive")           