def isprime(n):
      if n==1:
            return False
      for i in range(2,n//2+1):
            if n%i==0:
                  return False
      return True
def strong(n):#11
      pp=n-2#9
      np=n+2#13
      while not isprime(pp):
            pp=pp-2#7
      while not isprime(np):
            np=np+2
      np=(np+pp)/2
      if n>np:
            return True
      return False
def mad(l,r):
      k=0
      for i in range(l,r):
            if isprime(i):
                  if strong(i):
                        k=k+1#1
      return k
n=int(input())
for i in range(n):
      l,r=map(int,input().split())
      k=mad(l,r)
      print(k)
            
