import tkinter
from pytube import YouTube

root = tkinter.Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("IT SOURCECODE Youtube Video Downloader")


tkinter.Label(root, text ='Youtube Video Downloader', font ='arial 20 bold').pack()

##enter link
link = tkinter.StringVar()

tkinter.Label(root, text ='Paste Link Here:', font ='arial 15 bold').place(x= 160, y = 60)
link_enter = tkinter.Entry(root, width = 70, textvariable = link).place(x = 32, y = 90)



#function to download video


def Downloader():
     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    tkinter.Label(root, text ='DOWNLOADED', font ='arial 15').place(x= 180, y = 210)


tkinter.Button(root, text ='DOWNLOAD', font ='arial 15 bold', bg ='blue', padx = 2, command = Downloader).place(x=180, y = 150)



root.mainloop()
