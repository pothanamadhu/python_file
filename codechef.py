n=int(input())
for i in range(n):
      data=list(map(str,input().split()))
      x,y=map(str,input().split())
      i=data.index(x)
      j=data.index(y)
      if i<j:
            print(x)
      else:
            print(y)
