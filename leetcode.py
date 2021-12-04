n1=input()
n2=input()
if len(n1)==len(n2):
      l=len(n1)
      i=1
      while i<=l:
            r=n1[0]
            if n1==n2:
                  print(True)
                  break
            n1=n1[1:]+r
            i=i+1
      else:
            print(False)
else:
      print(False)
