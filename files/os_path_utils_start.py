import imp
import os
from os import path
import datetime
from datetime import date, time, datetime
import time

def main():
    print("Item exists: " + str(path.exists("text.txt")))
    print("Item is a file: " + str(path.isfile("text.txt")))
    print("Item is directory: " + str(path.isdir("text.txt")))

    # work with file path
def getRealPath():
    print("Item path: " + str(path.realpath("text.txt")))
    print("Item path and name: " + str(path.split(path.realpath("text.txt"))))

    #  get modification time
def getModificationTime():
    t = time.ctime(path.getmtime("text.txt"))
    print(t)
    
# calculate how long ago the item was modified
def calculateModificationTime():
    td = datetime.now() - datetime.fromtimestamp(
        path.getmtime("text.txt")
    )
    print("It has been " + str(td) + " since the file was modified")
    print("Or, " + str(td.total_seconds()) + " seconds")

if __name__ == "__main__":
    main()