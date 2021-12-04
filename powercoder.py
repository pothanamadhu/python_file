n=int(input())
if n==1 or n==2:
      print(n)
else:
      i=0
      k=1
      while k<n:
            k=2**i
            i=i+1
      print(i-1,n)
