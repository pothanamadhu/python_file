n=input()
data=n.split()
data1=[]
for word in data:
      t1=word[-1]
      t2=word[:-1]
      t1=t1.upper()
      t1=t1+t2[::-1]
      data1.append(t1)
print(" ".join(data1))
