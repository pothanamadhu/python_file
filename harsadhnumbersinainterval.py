def harshadh(n):
      p=n
      s=0
      while n:
            r=n%10
            n=n//10
            s=s+r
      if(p%s==0):
            return True
      else:
            return False
n=int(input())
for i in range(1,n+1):
      if(harshadh(i)):
            print(i)

