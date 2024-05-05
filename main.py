from pathlib import Path, PurePath
from datetime import *
from os import walk
import shutil
import os
from os.path import isfile, join



def organize(path: str):
    dirnames = [d for d in os.listdir(path) if not os.path.isfile(join(path, d)) and not d.startswith ('.')]
    movedItemCount = 0
    ignoredFiles = []
    yearFormatCharNumber = 4
    files = [f for f in os.listdir(path) if os.path.isfile(join(path, f)) and (f.endswith('.png') or f.endswith('.jpg') or f.endswith('.jpeg'))]
    
    print("dirs", dirnames)
    print("files", files)

    if(len(files)==0):
        print("No files found")
        return

    for filename in files:    
        print("Processing file", filename)
        if any(x.startswith(filename[:yearFormatCharNumber]) for x in dirnames):
            print("folder exists, moving", filename)
            try:
                shutil.move(str(PurePath(path,filename)), str(PurePath(path,filename[:yearFormatCharNumber],filename)))
                movedItemCount += 1
            except Exception as err:
                print('Error could not move file ', filename, err)
        else:
            print("Folder does not exists creating folder first", filename[:yearFormatCharNumber])
            try:
                os.mkdir(PurePath(path,filename[:yearFormatCharNumber]))
                dirnames.append(filename[:yearFormatCharNumber])
                shutil.move(str(PurePath(path,filename)), str(PurePath(path,filename[:yearFormatCharNumber])))
                movedItemCount += 1
            except Exception as err:
                print(f'Error could not create folder {filename[:yearFormatCharNumber]} or move file {filename} : \n', err)
    
    print(f'Task Done, moved {movedItemCount} files(s)')
    if len(ignoredFiles) != 0:
        print('Skipped these files : ', ignoredFiles)




def main():
    path = sys.argv[1]
    if not path:
        print("Pass a global path")
    if path == "":
        path = '.'
    print('received path : ', path)
    organize(path)

if __name__ == "__main__":
    main()