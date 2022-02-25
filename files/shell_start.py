import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    if path.exists("text.txt"):
        scr = path.realpath("text.txt")
        dst = scr + ".bat"
        
        # copy file
        # shutil.copy(scr, dst)
        # shutil.copystat(scr, dst)
        
        # renameFile()

        # now put things into a ZIP archive
        root_dir, tail = path.split(scr)
        shutil.make_archive("archive", "zip", root_dir)

    # more fine-grained control over ZIP file
    # with ZipFile("textzip.zip", "w") as newzip:
    #     newzip.write("text.txt")


def renameFile():
    os.rename("textfile.txt", "text.txt")
    print("ok")

if __name__ == "__main__":
    main()