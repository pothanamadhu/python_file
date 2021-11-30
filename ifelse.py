a,b,c,d,e,f=map(int,input().split())
w=0
if(a>=35):
      if a>=75:
            grade="A"
      elif a>=65:
            grade="B"
      elif a>=55:
            grade="C"
      else:
            grade="D"
      print("english",a,"P",grade)
else:
      w=w+1
      print("english",a,"F")
a=b
if(a>=35):
      if a>=75:
            grade="A"
      elif a>=65:
            grade="B"
      elif a>=55:
            grade="C"
      else:
            grade="D"
      print("tel",a,"P",grade)
else:
      w=w+1
      print("tel",a,"F","F")
a=c
if(a>=35):
      if a>=75:
            grade="A"
      elif a>=65:
            grade="B"
      elif a>=55:
            grade="C"
      else:
            grade="D"
      print("hindi",a,"P",grade)
else:
      w=w+1
      print("hindi",a,"F","F")
a=d
if(a>=35):
      if a>=75:
            grade="A"
      elif a>=65:
            grade="B"
      elif a>=55:
            grade="C"
      else:
            grade="D"
      print("math",a,"P",grade)
else:
      w=w+1
      print("math",a,"F","F")
a=e
if(a>=35):
      if a>=75:
            grade="A"
      elif a>=65:
            grade="B"
      elif a>=55:
            grade="C"
      else:
            grade="D"
      print("ss",a,"P",grade)
else:
      w=w+1
      print("ss",a,"F","F")
a=f
if(a>=35):
      if a>=75:
            grade="A"
      elif a>=65:
            grade="B"
      elif a>=55:
            grade="C"
      else:
            grade="D"
      print("Sci",a,"P",grade)
else:
      w+=1
      print("Sci",a,"F","F")
print("failed subs count =",w)
