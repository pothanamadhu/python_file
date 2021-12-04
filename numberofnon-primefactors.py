def non_prime(p):
      if p==1:
            return 1
      for i in range(2,p//2+1):
            if p%i==0:
                  return 1
      return 0      
n=int(input())
k=0
for i in range(1,n+1): 
      if n%i==0 and non_prime(i):
            k=k+1
print(k)
      

