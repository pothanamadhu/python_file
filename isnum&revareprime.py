def reverse(n):
      r=0
      s=0
      while(n):
            r=n%10
            n=n//10
            s=s*10+r
      return s
def isprime(n):
      if(n==1):
            return False
      for i in range(2,n//2+1):
            if(n%i==0):
                  return False
            return True
n=int(input())
num=isprime(n)
rev=reverse(n)
numrev=isprime(rev)
if(num and numrev):
      print("coprime")
else:
      print("not a coprime")
      
