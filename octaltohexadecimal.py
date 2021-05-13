n=int(input())
k=h=3
s=n
r=p=0
kata=[]
data=[]
pata=[]
while n:#12
      r=n%10#2
      if r>=8:
            h=0
            break
      n=n//10#1
      while k:#3
            p=r%2#0
            r=r//2
            kata.append(p)
            k=k-1#2
      k=3
l=len(kata)
for i in range(l):
      pata.append(kata[i])
pata.reverse()
l=len(pata)-1
while l:
      r=r+pata[l]*(2**p)
      p=p+1
      if p==4:
            if r<=9:
                        data.append(r)
            elif r==10:
                        data.append("A")
            elif r==11:
                        data.append("B")
            elif r==12:
                        data.append("C")
            elif r==13:
                        data.append("D")
            elif r==14:
                        data.append("E")
            else:
                        data.append("F")
            r=0
            p=0
      l-=1
data.reverse()
if h:
      print(*data)
else:
      print("given number is not a octal number")
            

"""=r=p=m=0
while  n:
      r=n%10
      n=n//10
      s=s*10+r
x=s
while s:
      r=s%10000
      s=s//10000
      while r:
            p=r%10
            r=r//10
            m=m*(2**l)
            if r==0:
                  if m<=9:
                        data.append(m)
                  elif m==10:
                        data.append("A")
                  elif m==11:
                        data.append("B")
                  elif m==12:
                        data.append("C")
                  elif m==13:
                        data.append("D")
                  elif m==14:
                        data.append("E")
                  else:
                        data.append("F")
            l=l+1
      l=0
print(*data)
"""


            
            
            


            
