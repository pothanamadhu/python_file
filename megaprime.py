def isprime(n):
      for i in range(2,n//2+1):
            if(n%i==0):
                  return False
            return True
n=int(input())
res=isprime(n)
#while(isprime(n%10) and res):
#      n=n//10
#else:
#      print("not a mega prime")
print("mega prime")
else:
      print("not a prime")
            
            
