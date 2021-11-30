n=int(input())
p=n
s=0
while n:
      r=n%10
      n=n//10
      s=s*10+r
if s==p:
      print("true")
else:
      print("false")
