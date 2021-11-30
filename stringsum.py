s=input()
k=int(input())
st=""
for i in s:
      st=st+str((ord(i)-96))
for i in range(k):
      pk=0
      for j in st:
            pk=pk+int(j)
      st=str(pk)
print(st)
      
