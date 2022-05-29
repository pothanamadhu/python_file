a=int(input())
b=int(input())
c=int(input())
k=int(input())
m1=max(a,b,c)
m3=min(a,b,c)
m2=a+b+c-m1-m3
if m1%3!=0:
      r=m1%3
      m1=m1+(3-r)
      k=k-(3-r)
if m2!=m1:
      r=m1-m2
      k=k-r
if m3!=m1:
      r=m1-m3
      k=k-r
if k!=0:
      print("No")
else:
      print("Yes")
      


      
