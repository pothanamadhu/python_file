n=input()
t=0
for i in range(len(n)):
      for j in range(i+1):
            l=n[j:len(n)-i]
            print(l)
