n=int(input())
d=[]
while n:
      r=n%10
      n=n//10
      d.append(r)
s=0
d.sort()
for i in d:
      s=s*10+i
print(s)

      
