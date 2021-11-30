n=int(input())
for i in range(n):
      d,r,t=map(int,input().split())
      if d<r:
            print("Too Early")
      elif d>t:
            print("Too Late")
      else:
            print("Take second dose now")
            
