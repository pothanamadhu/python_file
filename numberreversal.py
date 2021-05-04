def reverse(n):
      r=0
      s=0
      while(n):
            r=n%10
            n=n//10
            s=s*10+r
      return s
n=int(input())
rev=reverse(n)
print("the revese of",n,"is",rev)
