def flames(m1,n1,o1):
      c=0
      for i in m1:
            if i not in n1:
                  c=c+1
      for j in m1:
            if j not in o1:
                  c=c+1
      for x in n1:
            if j not in m1:
                  c=c+1
      for y in n1:
            if j not in o1:
                  c=c+1
      for z in o1:
            if j not in m1:
                  c=c+1
      for v in o1:
            if j not in n1:
                  c=c+1
      return c
def madhu(data,l,r):
      k=r%l
      data.remove(data[k-1])
m1=list(map(str,input().split()))
n1=list(map(str,input().split()))
o1=list(map(str,input().split()))
data=["f","l","a","m","e","s"]
r=flames(m1,n1,o1)
while(len(data)!=1):
      madhu(data,len(data),r)
print(*data)
      
