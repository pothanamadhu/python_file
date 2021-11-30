n=input()
d=[]
h=[]
for i in n:
      if ord(i)%2==0:
            d.append(i)
      else:
            h.append(i)
print("even  :",d)
print("odd  :",h)
