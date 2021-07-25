def pairs(data,n):
      d={}
      l=0
      for i in data:#10 20 30 10 10 20 10 40 20
            if i not in d.keys():
                  d[i]=1
            else:
                  d[i]+=1
      #10;4 20;3 30;1 40;1
      for k,v in d.items():
            if v>1:
                  l=l+(v//2)#2+1
      return l
n=int(input())
data=list(map(int,input().strip().split()))
k=pairs(data,n)
print(k)
"""
10 20 30 10 10 20 10 30 20
2+1+1
4
4//2=2
3//2=1
"""
"""
3
1 2 3
4 5 6
7 8 9
"""
