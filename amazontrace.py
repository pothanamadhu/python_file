n,m=map(int,input().split())
data=[]
for i in range(n):
    d=list(map(int,input().split()))
    data.append(d)
q=0
for i in data:
    for j in i:
        if j==9:
            q=1
i=j=0
if q==0 or data[0][0]==0:
    print("-1")
    q=0
if data[0][0]==9:
    print("0")
    q=0 
k=0
while q:
    if data[i][j]==9:
        break
    elif (i+1<n and data[i+1][j]==9) or (j+1<m and data[i][j+1]==9):
        k=k+1
        break
    elif i+1<n and data[i+1][j]==1:
        i=i+1
        k=k+1
    elif j+1<m and data[i][j+1]==1:
        j=j+1
        k=k+1
    else:
        k=-1
m=k
k=0
i=j=0
while q:
    if data[i][j]==9:
        break
    elif (i+1<n and data[i+1][j]==9) or (j+1<m and data[i][j+1]==9):
        k=k+1
        break
    elif j+1<m and data[i][j+1]==1:
        i=i+1
        k=k+1
    elif i+1<n and data[i+1][j]==1:
        j=j+1
        k=k+1
    else:
        k=-1
if q==1:
    print(min(m,k))
