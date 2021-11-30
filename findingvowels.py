n=input()
s=""
for i in n:
      if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
            s=s+i
      else:
            if len(s)>1:
                  print(s)
            s=""
if len(s)>0:
            print(s)
