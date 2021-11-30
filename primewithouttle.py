def prime(n):
      a=2
      k=0
      p=[1 for i in range(n)]
      while a*a<=n:
            if(p[a]==1):
                  for i in range(a*a,n,a):
                        p[i]=0
            a=a+1
      print(p)
      return p.count(1)-2
n=int(input())
print(prime(n))
