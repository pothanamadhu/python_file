n=[1,2,1,3]
d={}
for i in n:
      if i not in d.keys():
            d[i]=1
      else:
            d[i]+=1
print(d)
#{1;2,2;1,3;1}
