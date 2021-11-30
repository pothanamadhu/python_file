n=input()
s=""
for i in n:
      if i!=" ":
            if len(s)==0:
                  s=s+i.upper()
            else:
                  s=s+i
      else:
            if s.count(" ")!=len(s):
                  print(s)
            s=""
if s.count(" ")!=len(s):
                  print(s)
