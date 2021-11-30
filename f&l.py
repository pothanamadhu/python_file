def count(n):
      c=0
      while n:
            n=n//10
            c=c+1
      return c
n=int(input())
c=count(n)
l=n%10
f=n//(10**(c-1))
i=r=s=0
k=c
while n:
      r=n//(10**(c-1))
      n=n%(10**(c-1))
      if i==0:
            s=s*10+l
      elif i==k-1:
            s=s*10+f
      else:
            s=s*10+r
      i=i+1
      c=c-1
print(s)
