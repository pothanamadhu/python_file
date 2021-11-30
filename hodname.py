n=input()
j=0
for i in range(len(n)-1,-1,-1):
      for k in range(j+1):
            if k==j:
                  print(n[i])
            else:
                  print("  ",end=" ")
      j=j+1

      
