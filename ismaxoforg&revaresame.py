def findmaxpos(data,n):
      mi=0
      m=data[0]
      for i in range(1,n):
            if(m<data[i]):
                  m=data[i]
                  mi=i
      return mi

def reverse(data,n):
      r=0
      s=0
      for i in range(n):
            k=data[i]
            while(k):
                  r=k%10
                  k=k//10
                  s=s*10+r
            data[i]=s
            s=0
n=int(input())
data=list(map(int,input().split()))
m1=findmaxpos(data,n)
reverse(data,n)
if(m1==m2):
      print("perfect")
else:
      print("imperfect")

