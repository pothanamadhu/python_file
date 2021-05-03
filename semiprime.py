def isprime(n):
      if(n==1):
            return 0
      for i in range(2,n):
            if(n%i==0):
                  return 0
            return 1
n=int(input())
p=isprime(n)
