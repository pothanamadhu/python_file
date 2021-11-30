n=int(input())
a=0
b=1
c=0
if n==0 or n==1:
      print(n)
while 1:
      c=a+b
      a=b
      b=c
      if c==n:
            print(c)
            break
      if(c>n):
            if(n-a==c-n):
                  print(a,c)
            elif(n-a>c-n):
                  print(c)
            else:
                  print(a)
            break
      
