import csv
import matplotlib.pyplot as plt
import numpy as np
b=[]
d={}
e={}
w=[]
p=[]
q=[]
m=[]
n=[]
with open("real_data.csv")as f1:
      data=list(csv.reader(f1))
      for i in data[1:]:
            w.append(i[2])
      for i in w:
            if i not in e.keys():
                  e[i]=1
            else:
                  e[i]+=1
      for i in data[1:]:
            if i[6]=="Evening":
                  b.append(i)
      for i in b:
            if i[2] not in d.keys():
                  d[i[2]]=1
            else:
                   d[i[2]]+=1
      print(d)
      print(e)
      for k,v in d.items():
            p.append(k)
            q.append(v)
      for k,v in e.items():
            m.append(k)
            n.append(v)
x=np.array(p)
y=np.array(q)
s=np.array(m)
t=np.array(n)
plt.plot(x,y)
plt.plot(s,t)
plt.show()
"""
axs = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
axs[0].plot(x, y)
axs[1].plot(x, -y)
"""


                  
            
