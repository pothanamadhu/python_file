n=int(input())
data=[]
d=0
while(n):#10 5 2 1
      d=n%2
      n=n//2
      data.append(d)#0 1 0 1#5 2 1
data.reverse()
print(*data)
