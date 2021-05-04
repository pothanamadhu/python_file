def isprime(n):
      if(n==1):
            return False
      for i in range(2,n//2+11):
            if(n%i==0):
                  return False
      return True
n=int(input())
t=isprime(n)
k=0
for p in range(2,n+1):
      if(isprime(p)):
            k=k+1
if(t and isprime(k)):
      print("sp")
else:
      print("not a sp")
      

