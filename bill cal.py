u=int(input())
if u<=200:
      b=u*1.20
elif u>200 and u<400:
      b=u*1.50
elif u>=400 and u<600:
      b=u*1.80
else:
      b=u*2
      
if b>400:
      b=(b/100)*15+b
print(b)
