import os
from Tkinter import *

def findFiles(directory,fileList):
    fileList.delete(0,END)
    objects = os.listdir(os.path.expanduser(directory))
    for i in objects:
        if isFile(directory + i):
            fileList.insert(END,i)
        else:
            fileList.insert(END,"/"+i)

def isFile(object):
    try:
        os.listdir(os.path.expanduser(object))
        return False
    except Exception:
        return True