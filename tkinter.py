from tkinter import *
from tkinter import messagebox
top=Tk()
top.geometry("600x400")

def get_data():
      tb3.configure(state="normal")
      a=int(tb1.get())
      b=int(tb2.get())
      tb1.delete(0,END)
      tb2.delete(0,END)
      l3.configure(text="result="+str(a+b))
      tb3.delete(0,END)
      tb3.insert(0,a+b)
      tb3.configure(state="disabled")
      messagebox.showinfo("result",str(a+b))

l1=Label(top,text="enter data")
l1.pack()
tb1=Entry(top,width=70)
tb1.pack()

l2=Label(top,text="enter data")
l2.pack()
tb2=Entry(top,width=70)
tb2.pack()

b1=Button(top,text="submit",command=get_data)
b1.pack()

l3=Label(top)
l3.pack()

l4=Label(top,text="result")
l4.pack()

tb3=Entry(top,width=70)
tb3.pack()
