from math import *
def div(n):
      k=0
      s=int(sqrt(n))
      for i in range(1,s+1):
            if n%i==0:
                  if(i!=n//i):
                        k=k+i+n//i
                  else:
                        k=k+i
      return k
n=int(input())
s=int(sqrt(n))
k=0
if(n==1):
      k=1
else:
      for i in range(1,s+1):
            if n%i==0:
                  if(i!=n//i):
                        k=k+div(i)
                        print(i,div(i))
                        k=k+div(n//i)
                        print(n//i,div(n//i))
                  else:
                        k=k+div(i)
                        print(i,div(i))
print(k)
