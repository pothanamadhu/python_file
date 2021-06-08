import tkinter
from tkinter import *
import random
from tkinter import messagebox
from random import shuffle

answer=["python","google","yahoo","india"]# add number of words here
words=[]
for i in answer:
    word=list(i)
    shuffle(word)
    words.append(word)
num=random.randint(0,len(words)-1)
score=0
def initial():
    global words,num,score
    lb1.configure(text=words[num])
    lb2.configure(text=score)
    
def ans_check():
    global words,num,answer,score
    user_input=e1.get()
    if user_input==answer[num]:
        score+=10
        lb2.configure(text=score)
        messagebox.showinfo("sucess","right")
        reset()
    else:
        messagebox.showinfo("Error","wrong")
        score-=10
        lb2.configure(text=score)
        e1.delete(0,END)
def reset():
    global words,num,answer
    num=random.randint(0,len(words)-1)
    lb1.configure(text=words[num])
    e1.delete(0,END)
    e1.delete(0,END)
    
root=tkinter.Tk()
root.geometry("400x400")

lb2=Label(root,font='times 20')
lb2.pack(pady=30,ipady=10,ipadx=10)
lb1=Label(root,font='times 20')
lb1.pack()




ans=StringVar()
e1=Entry(root,textvariable=ans)
e1.pack(ipady=5,ipadx=5)
b1=Button(root,text="check",width=20,command=ans_check)
b1.pack(pady=40)
b2=Button(root,text="Reset",width=20,command=reset)
b2.pack()
initial()
root.mainloop()
