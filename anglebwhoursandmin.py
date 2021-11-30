h,m=map(int,input().split())
mins=m*6
hrs=h*30+m/2
if(hrs>mins):
      p=hrs-mins
else:
      p=mins-hrs
if p>360-p:
      print(360-p)
else:
      print(p)
      
