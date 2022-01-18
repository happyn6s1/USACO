bs=[".....","...X.","...X.","...X.","....."]
m=len(bs)
n=len(bs[0])
import heapq
M=[[0 for j in range(m)] for i in range(n)]
hq=[]
for i in range(m):
    for j in range(n):
        k=6
        if i<=1:
            k-=(2-i)
        if j<=1:
            k-=(2-j)
        if i>=m-2:
            k-=(i-m+3)
        if j>=n-2:
            k-=(j-m+3)
        heapq.heappush(hq,(-k,i,j))
        M[i][j]=k
ans=[]
INF=9999
nn=0
while hq:
    p=heapq.heappop(hq)
    if M[p[1]][p[2]]==0:
        continue
    nn+=1
    print(nn,p,ans,hq[0])
    i=p[1]
    j=p[2]
    if bs[p[1]][p[2]]=="X":
        ans.append((p[1],p[2]))
        if len(ans)==3:
            print(ans)
            break
        for ii in [-2,-1,1,2]:
            if i+ii>=0 and i+ii<=m-1:
                M[i+ii][j]+=(3-abs(ii))
                heapq.heappush(hq,(-M[i+ii][j],i+ii,j))
            if j+ii>=0 and j+ii<=m-1:
                M[i][j+ii]+=(3-abs(ii))
                heapq.heappush(hq,(-M[i][j+ii],i,j+ii))
                        
    else:
        M[i][j]=0
        heapq.heappush(hq,(0,i,j))
        
print(ans)
