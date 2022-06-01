n,b,c=map(int,input().split())
d=list(map(int,input().split()))
k=0
for i in range(n):
      for j in range(n-i):
            p=d[j:j+i+1]
            if sum(p)>=b and sum(p)<=c:
                  k=k+1
print(k)
