def binary(n):
      d=0
      k=0
      tata=[]
      while(n):#2
            d=n%2#0
            n=n//2#1
            tata.append(d)#0 01
      tata.reverse()
      return tata
n=int(input())
r=0
data=[]
while(n):
      r=n%10
      n=n//10
      data.append(binary(r))
data.reverse()
print(*data)
