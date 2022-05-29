def processArray(data):
      for i in data:
            if i<55 and i%10==6:
                  print(-5)
            elif i<55:
                  print(-4)
            elif i%10==6:
                  print(-2)
            else:
                  print(i)
data=list(map(int,input().split()))
processArray(data)
