
from Tkinter import *
import os
import ftplib
import FileOperations
#server.login('daemon','xampp')

def connectServer(IP,username,password,serverFileList):
    serverFileList.delete(0,END)


    try:
        server = ftplib.FTP()
        server.connect(IP,21)
        server.login(username,password)
        #server.cwd('/webalizer')
        serverFolderList = server.nlst()
        for i in serverFolderList:
            serverFileList.insert(END,i)
        server.close()
    except:
        errorBox = Tk()
        errorMessage = Label(errorBox,text="Connection Error",width=30).pack()




def uploadServer(IP,username,password,serverFileList,directory,selectFile):
    server = ftplib.FTP()
    server.connect(IP,21)
    server.login(username,password)
    #server.cwd('/webalizer')
    file = open(os.path.expanduser(directory)+"/"+selectFile,'rb')
    server.storbinary('STOR '+selectFile,file)
    file.close()
    server.close()
    connectServer(IP,username,password,serverFileList)

def downloadServer(IP,username,password,directory,fileList,serverFileList):
    selectFile=serverFileList.get(serverFileList.curselection())
    server = ftplib.FTP()
    server.connect(IP,21)
    server.login(username,password)
    #server.cwd('/webalizer')
    localfile = open(os.path.expanduser(directory)+"/"+selectFile,'wb')
    server.retrbinary('RETR '+ selectFile,localfile.write,1024)
    server.close()
    localfile.close()
    FileOperations.findFiles(directory,fileList)

def deleteServer(IP,username,password,serverFileList):
    selectFile=serverFileList.get(serverFileList.curselection())
    server = ftplib.FTP()
    server.connect(IP,21)
    server.login(username,password)
    #server.cwd('/webalizer')
    server.delete(selectFile)
    server.close()
    connectServer(IP,username,password,serverFileList)

def inputValue(IP,username,password,serverFileList):
    global inputbox
    inputbox = Tk()
    enterValueLabel = Label(inputbox,text="Enter File New Name").pack()
    newNameValue = Entry(inputbox,width=20)
    newNameValue.pack()
    submitButton = Button(inputbox,text="OK",command=lambda:okButton(IP,username,password,newNameValue.get(),serverFileList),width=10).pack()

def okButton(IP,username,password,str,serverFileList):

    selectFile=serverFileList.get(serverFileList.curselection())
    server = ftplib.FTP()
    server.connect(IP,21)
    server.login(username,password)
    #server.cwd('/webalizer')
    server.rename(selectFile,str)
    server.close()
    connectServer(IP,username,password,serverFileList)
    inputbox.destroy()
