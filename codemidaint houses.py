n=int(input())
l=[]
for i in range(n):
      n1,n2,n3=map(int,input().split())
      l.append([n1,n2,n3])
w=min(l[0])
j=l[0].index(w)
for i in range(1,n):
      data=l[i]
      if j==0:
            p=min(data[1],data[2])
            w=w+p
            j=data.index(p)
      elif j==1:
            p=min(data[0],data[2])
            w=w+p
            j=data.index(p)
      else:
            p=min(data[0],data[1])
            w=w+p
            j=data.index(p)
print(w)
