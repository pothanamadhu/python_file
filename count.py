s=input()
s=list(s.split())
data=[]
k=0
for i in s:
      if not i.isdigit():
            for j in i:
                  if (ord(j)>=97 and ord(j)<=122) or  (ord(j)>=65 and ord(j)<=90) or ord(j)==33 or ord(j)==46 or ord(j)==44 or ord(j)==63 or ord(j)==45:
                        n=1
                  else:
                        print(i)
                        break
            else:
                  k=k+1
print(k)
            
