n,sv,rv=map(int,input().split())
k=1
s=r=0
while n:
      r=n%10
      n=n//10
      s=s*10+r
n=s
s=r=0
while n:
      r=n%10
      n=n//10
      if r%sv==0:
            r=rv
            rv=rv+1
      s=s+r*k
      k=k*10
n=s
r=s=0
while n:
      r=n%10
      n=n//10
      s=s*10+r
print(s)
