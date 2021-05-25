from tkinter import *
import random
top=Tk()
top.geometry("600x400")
def get_data():
      data=[["4M1","4M2","4M3"],["4M4","4M5","4M6"],["4M7","4M8","4M9"],["4N1","4N2","4N3"],["4N4","4N5","4N8"]]
      p=random.choice(data)
      q=random.choice(p)
      r=data.index(p)
      data.remove(p)
      l1.configure(text="group is " +str(r+1) + " and the student is " + str(q))
b1=Button(top,text="choose",command=get_data)
b1.pack()
l1=Label(top,text="output")
l1.pack()




