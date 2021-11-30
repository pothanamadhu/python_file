n=int(input())
inr=int(input())
h=int(input())
t=0
for j in range(h):
      y1,m1,d1,am=map(int,input().split())
      for m in range(y1*360+m1*30+d1):
            n=n+(n*inr)/36000
      n=n-am
print(n)
