n=int(input())
data=[]
for i in range(n):
      d=list(map(str,input().split()))
      data.append(d)
data.sort()
for i in data:
      print(i)
