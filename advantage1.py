def prime(n):
      m=n
      t,k=2,0
      while t<=n:
            if n%t==0:
                  k=k+t
                  n=n//t
            else:
                  t=t+1
      return k==m
def pd(n):
      k=0
      for i in range(2,n+1):
            if prime(i):
                  k=k+1
      return k
n=int(input())
print(pd(n))
