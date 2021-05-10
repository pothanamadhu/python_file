def sums(n):
      r=0
      s=0
      while n:
            r=n%10
            n=n//10
            s=s+r
            if(n==0 and s>9):
                  n=s
                  s=0
      return s
n=int(input())
s=sums(n)
print(s)
