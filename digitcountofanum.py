n=int(input())
e=0
o=0
while n:
      r=n%10
      n=n//10
      if(r%2==0):
            e=e+1
      else:
            o=o+1
if(e%2==0 and o%2==1):
      print("even odd")
elif(e%2!=0 and o%2==1):
      print("odd")
elif(e%2==0 and o%2!=1):
      print("even")
else:
      print("mixed")
      
