def pd(n):
      s=n
      k=0
      while n:
            r=n%10
            n=n//10
            k=k*10+r
      if k==s:
            return True
      return False
n=int(input())
n1=n-1
n2=n+1
while(1):
      if pd(n1):
            print(n1)
            break
      if pd(n2):
            print(n2)
            break
      n1=n1-1
      n2=n2+1

      
