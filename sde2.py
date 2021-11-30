def mad(n):
      s=""
      while n:
            r=n%2
            n=n//2
            s=str(r)+s
      
      return s
n=int(input())
k=[]
for i in range(1,n+1):
      k.append(mad(i))
print(*k)
