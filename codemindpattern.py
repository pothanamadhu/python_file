n=input()
d={}
for i in n:
      if i not in d.keys():
            d[i]=1
      else:
            d[i]+=1
p=0
for k,v in d.items():
      if v==1:
            p=p+1
            if p==2:
                  print(k)
                  break
else:
      print("in")

