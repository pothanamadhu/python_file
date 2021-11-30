n,m=map(int,input().split())
data=list(map(int,input().split()))
k=0
l=data[m-1]
for i in data:
      if i>=l and i>0:
            k=k+1
print(k)
