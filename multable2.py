n,r1,r2=map(int,input().split())
if(r1>r2):
      range=range(r1,r2+1)
else:
      range=range(r1,r2-1,-1)
for i in range:
      print(n,"X",i,"=",i*n)
