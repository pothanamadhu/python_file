n=int(input())
for i in range(n):
      l,r=map(int,input().split())
      p=0
      for j in range(l,r+1):
            print(j)
            h=j%10
            if h==2 or h==3 or h==9:
                  p=p+1
                  print(j,"joythi")
      print(p)
