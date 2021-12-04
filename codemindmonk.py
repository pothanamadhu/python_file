t=int(input())
for i in range(t):
      n,m=map(int,input().split())
      if n==0:
            print(0)
      else:
            for j in range(n):
                  if (2*j)%m==n:
                        print(j)
                        break
            else:
                  print(-1)
