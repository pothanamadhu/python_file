m,n=map(int,input().split())
data=[]
for anil in range(m):
      temp=list(map(str,input().split()))
      if anil%2:
            temp.reverse()
      data.extend(temp)
t=int(input())
product=input()
leng=n*m
t=t%leng
z=0
res=data[leng-t:]+data[:leng-t]
po=0
flag=1
q=[]
for i in res:
      po=po+1
      q.append(i)
      if flag==1 and po%n==0:
            print(*q)
            q=[]
            flag=0
      elif flag==0 and po%n==0:
            q.reverse()
            print(*q)
            q=[]
            flag=1
if product in res:
      j=res.index(product)
      row=j//n
      col=j%n
      if row%2:
            col=n-col-1
else:
      z=1
if z==1:
      print("Not Available")
else:
      print([row,col])

