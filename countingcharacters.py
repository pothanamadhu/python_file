n=input()
k=1
n=n+"\n"
for i in range(len(n)-1):
      if n[i]==n[i+1]:
            k=k+1
      else:
            print("(",k,",",n[i],")",end=" ")
            k=1
      
