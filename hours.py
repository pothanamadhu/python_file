h=int(input())
if h<=5:
      print(h)
else:
      if h<24:
            k=h-5
            n=k*0.5+5
      else:
            n=h%24
            n=h//24*15+n*0.5
      print(n)

      
