def isvalid(i,j,n,m,l):
    if i>=0 and i<n and j>=0 and j<m and l[i][j]!=0:
        return 1
    return 0
n,m=map(int,input().split())
l=[]
for i in range(n):
    a=list(map(int,input().split()))
    l.append(a)
if l[0][0]==0:
    print(-1)
elif l[0][0]==9:
    print(0)
else:
    ans=[]
    ans.append([0,0,0])
    vis=[]
    for i in range(n):
        r=[0]*m
        vis.append(r)
    vis[0][0]=1
    di=[-1,0,1,0]
    dj=[0,1,0,-1]
    flag=0
    while(len(ans)>0):
        if(flag==-1):
            break
        i=ans[0][0]
        j=ans[0][1]
        step=ans[0][2]
        for k in range(4):
            newi=di[k]+i
            newj=dj[k]+j
            if(isvalid(newi,newj,n,m,l) and vis[newi][newj]==0):
                if l[newi][newj]==9:
                    print(step+1)
                    flag=-1
                    break
                vis[newi][newj]=1
                ans.append([newi,newj,step+1])
        ans.pop(0)
        
    if(flag==0):
        print(-1)
