def octal(n):
      s=0
      r=0
      i=0
      while(n):#11
            r=n%10#1
            n=n//10#1
            p=r*(2**i)#2
            s=s+p#1+2
            i=i+1#1
      return s
n=int(input())
r=0
s=[]
while(n):
      r=n%1000
      s.append(octal(r))
      n=n//1000
s.reverse()
print(*s)

      
