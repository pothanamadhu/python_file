n=int(input())
p=n
s=0
while n:
      r=n%10
      n=n//10
      s=s+r
if(p%s==0):
      print("harsadh number")
else:
      print("not a harsadh number")
      
