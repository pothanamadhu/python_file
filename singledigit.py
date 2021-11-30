n=int(input())
k=0
while n:
      r=n%10
      n=n//10
      k=k+r
      if n==0 and k>9:
            n=k
            k=0
print(k)
