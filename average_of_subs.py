n=int(input('roll number'))
m=int(input('physics marks'))
o=int(input('chemistry marks'))
p=int(input('computer science'))
t=m+o+p
per=t/3
if per>80:
      print('first')
elif per>70 and per<79:
      print('second')
elif per>60 and per<69:
      print('third')
elif per>50 and per<59:
      print('fourth')
else:
      print('fail')
print(t,per,sep='\n')
