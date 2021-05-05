import math
l,b=map(float,input().split())
area=l*b
peri=2*(l+b)
dia=math.cbrt(l**2+b**2)
print("%.2f"%area,"%.2f"%peri,"%.2f"%dia)
