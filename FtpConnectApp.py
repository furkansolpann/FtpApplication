from Tkinter import *
import FtpOperations
import FileOperations
#btn = Button(root,text="tikla",command=lambda:upper(thelabel))


def onselect(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print 'You selected item %d: "%s"' % (index, value)



def main():


    root = Tk()
    directory = "~/"
    ftpLabel = Label(root, text="Enter FTP Adress:")
    ftpLabel.grid(sticky="W",row=0,column=0)
    ftpAdress = Entry(root, width=30)
    ftpAdress.grid(sticky="E",row=0,column=0)
    nameLabel = Label(root, text="Enter Username:")
    nameLabel.grid(sticky="W",row=1,column=0)
    username = Entry(root, width=30)
    username.grid(sticky="E",row=1,column=0)
    passwordLabel = Label(root, text="Enter Password:")
    passwordLabel.grid(sticky="W",row=2,column=0)
    password = Entry(root, width=30)
    password.grid(sticky="E",row=2,column=0)


    myFilesLabel = Label(root, text="Computer Files")
    myFilesLabel.grid(sticky="W",row=3,column=0)
    ftpServerLabel = Label(root, text="FTP Server Files")
    ftpServerLabel.grid(sticky="E",row=3,column=1)
    myFilesList = Listbox(root,width=45,height=30)
    myFilesList.grid(sticky="W",row=4,column=0)
    FileOperations.findFiles(directory,myFilesList)
    myFilesList.bind('<Double-Button-1>', onselect)
    ftpServerList = Listbox(root,width=45,height=30)
    ftpServerList.grid(sticky="E",row=4,column=1)
    connectButton = Button(root,text="Connect",command=lambda:FtpOperations.connectServer(ftpAdress.get(),username.get(),password.get(),ftpServerList),width=10)
    connectButton.grid(sticky="W",row=2,column=1)
    uploadButton = Button(root,text="Upload Server",command=lambda:FtpOperations.uploadServer(ftpAdress.get(),username.get(),password.get(),ftpServerList,directory,myFilesList.get(myFilesList.curselection())),width=10)
    uploadButton.grid(sticky="W",row=5,column=0)
    downloadButton = Button(root,text="Download Server",command=lambda:FtpOperations.downloadServer(ftpAdress.get(),username.get(),password.get(),directory,myFilesList,ftpServerList),width=11)
    downloadButton.grid(sticky="W",row=5,column=1)
    renameButton = Button(root,text="Rename File Server",command=lambda:FtpOperations.inputValue(ftpAdress.get(),username.get(),password.get(),ftpServerList),width=13)
    renameButton.grid(row=5,column=1)
    deleteButton = Button(root,text="Delete Server",command=lambda:FtpOperations.deleteServer(ftpAdress.get(),username.get(),password.get(),ftpServerList),width=10)
    deleteButton.grid(sticky="E",row=5,column=1)


    root.mainloop()


main()