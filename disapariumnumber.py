n=int(input())
s=0
p=n
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
if(s==p):
      print("disaparium number")
else:
      print("not a disaparium number")
