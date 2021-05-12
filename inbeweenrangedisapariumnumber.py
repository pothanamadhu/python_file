def disaparium(n):
      p=n
      s=0
      while(n):#175
            r=n%10
            n=n//10
            s=s*10+r
      n=s
      s=r=0
      k=1
      while(n):#571
            r=n%10
            n=n//10
            s=s+r**k
            k=k+1
      return s
n=int(input())
o=disaparium(n)
i=1
l=0
while i<n:
      l=disaparium(i)
      if(i==l):
            print(i)
      i=i+1
      
