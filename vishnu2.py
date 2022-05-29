from itertools import permutations
n,k=map(int,input().split())
wap=[]
data=[]
for i in range(n):
      t=list(map(int,input().split()))
      wap.append(t)
p=list(permutations(wap,k))

