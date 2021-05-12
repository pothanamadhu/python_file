n,a,b=map(int,input().split())
k=1
s=0
while n:
      r=n%10
      n=n//10
      if r==a:
            r=b
      s=s+r*k
      k=k*10  
print(s)
