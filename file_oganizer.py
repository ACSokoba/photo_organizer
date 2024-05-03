# from shutil import move
from pathlib import Path, PurePath
from datetime import *
from os import walk
import shutil
import os


def organize() :
    fileNames = []
    dirnames = []
    movedItemCount = 0
    ignoredFiles = []

    for (dirpath, dirnames, filenames) in walk('.'):
        print("root dir  ", dirpath, " Found folders : ", dirnames, "files : ", fileNames)
        for filename in filenames:
            if filename.endswith('.pyc') or filename.endswith('.py'):
                ignoredFiles.append(filename)
                continue
            print("Processing file", filename)
            if any(x.startswith(filename[:4]) for x in dirnames):
                print("folder exists, moving", filename)
                try:
                    shutil.move(filename, PurePath('./'+ filename[:4] + '/' + filename))
                    movedItemCount += 1
                except Exception as err:
                    print('Error could not move file ', filename, err)
            else:
                print("Folder does not exists creating folder first", filename[:4])
                try:
                    os.mkdir(filename[:4])
                    shutil.move(filename, filename[:4])
                    movedItemCount += 1
                except Exception as err:
                    print(f'Error could not create folder {filename[:4]} or move file {filename} : \n', err)
        
        print(f'Done, moved {movedItemCount} files(s) \n Skipped these files {ignoredFiles}')


