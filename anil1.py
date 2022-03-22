def opQueue(q,queries):
      a=[]
      b=[]
      p=0
      for pa in queries:
            x1,x2=pa
            if x1==1:
                  a.append(x2)
            else:
                  p=a.pop(0)
            if x2==1 and p!=0:
                  a.append(p)
            elif x2==2 and p!=0:
                  b.append(p)
      k1=k2=1
      for i in a:
            k1=k1*i
      for i in b:
            k2=k2*i
      return k1+k2
print(opQueue(4,[[1,2],[1,2],[2,1],[2,2]]))
print(opQueue(3,[[1,3],[1,2],[2,2]]))
print(opQueue(5,[[1,2],[2,1],[1,5],[2,1],[2,2]]))
                  
