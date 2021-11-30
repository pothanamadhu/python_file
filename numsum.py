n=input()
g=""
k=t=0
for i in n:
      if ord(i)>=48 and ord(i)<=57:
            g=g+i
      elif len(g):
            for j in g:
                  t=t*10+(ord(j)-48)
            k=k+t
            g=""
            t=0
if len(g):
      for j in g:
            t=t*10+(ord(j)-48)
      k=k+t
print(k)
