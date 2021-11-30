import math
n,p=map(int,input().split())
s=int(math.sqrt(n))
data=[]
for i in range(1,s+1):
      if n%i==0:
            if i==n//i:
                  data.append(i)
            else:
                  data.append(i)
                  data.append(n//i)
data.sort()
if p>len(data):
      print(0)
else:
      print(data[p-1])
