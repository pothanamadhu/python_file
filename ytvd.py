from pytube import *
from tkinter import *
top=Tk()
top.geometry("400x200")
def yt():
      url=str(tb1.get())
      madhu=YouTube(url)
      madhu=madhu.streams.get_highest_resolution()
      madhu.download()
      l1.configure(text=str(madhu.title) + " was downloaded👍")
tb1=Entry(top,width=50)
tb1.pack()
b1=Button(top,text="Download",command=yt)
b1.pack()
l1=Label(top,text="processing")
l1.pack()
