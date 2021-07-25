def sums(n):
      temp=s=0
      for i in n:#1a2c25
            if i.isdigit():
                  temp=temp*10+int(i)#25
            else:
                  s=s+temp#1+2
                  temp=0
      s=s+temp
      return s                  
n=input()#1a2c25
k=sums(n)
print(k)
