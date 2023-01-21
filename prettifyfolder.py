#Oh soldier prettify my folder
# inputs: path, file name, format
import os
def soldier(path, file ,format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    with open(file) as a:
        filelist = a.read().split("\n")
    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())
        if os.path.splitext(file)[1] == format:
            os.rename(file, f"{i}.{format}")
            i += 1
# pathn = input(r"Enter the full path:")
# filen = input(r"Enter the file path which you have to rename:")
# ext = input("Enter the extension which you have to rename:")
# soldier(pathn,filen,ext)
soldier(r"D:\My Files\Personal", r"D:\Python_with_harry\harry-di.txt", ".png")



