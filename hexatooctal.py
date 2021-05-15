def octal(n):
      r=s=p=0
      while n:
            r=n%10
            n=n//10
            s=s+r*(2**p)
            p=p+1
      return s
n=int(input())
hexa=list(map(int,input().split()))
l=4
s=r=e=0
for i in hexa:
      while l:
            r=i%2
            i=i//2
            s=s*10+r
            l-=1
      e=s
      print(e)
      s=0
      l=4
print(s)
r=m=a=h=k=0
while s:
      r=s%10
      s=s//10
      k=k*10+r
print(k)
while k:
      r=k%1000
      k=k//1000
      h=h*10+(octal(r))
print(h)
"""
      h=h*10+a
      m=0
      a=0
print(h)
"""
      
