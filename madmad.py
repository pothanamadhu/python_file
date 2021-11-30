m,n=map(int,input().split())
if n%2==0:
      n=n//2
      p=n*m
else:
      n=n//2
      k=m//2
      p=n*m+k
print(p)
      
