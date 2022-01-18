"""
ID: happyn61
LANG: PYTHON3
PROB: loan
"""

#from collections import defaultdict
import sys
import heapq
from collections import deque

#fin = open ('loan.in', 'r')
#fout = open ('loan.out', 'w')
#print(dic["4734"])
def find(parent,i):


    if parent[i] != i: 
        parent[i]=find(parent,parent[i]) 
    return parent[i] 

        # A utility function to do union of two subsets 
def union(parent,rank,xx,yy): 
    x=find(parent,xx)
    y=find(parent,yy)
    if rank[x]>rank[y]:
        parent[y]=x
    elif rank[y]>rank[x]:
        parent[x]=y
    else:
        parent[y]=x
        rank[x]+=1
ans=0

NQ=sys.stdin.readline().strip().split()
n=int(NQ[0])
m=int(NQ[1])
BIG=99999999
g=[[] for i in range(n)]
visited=[False for i in range(n)]
ans=[(BIG,BIG,0) for i in range(n)]
ans[0]=[0,BIG,0]
for i in range(m):
    ABC=sys.stdin.readline().strip().split()
    a=int(ABC[0])-1
    b=int(ABC[1])-1
    c=int(ABC[2])
    heapq.heappush(g[a],(c,b))
    heapq.heappush(g[b],(c,a))
dq=deque([0])
visited[0]=True
while dq:
    t=dq.popleft()
    print(t)
 #   visited[t]=True
    for w,tt in g[t]:
        e=ans[t][0]+min(ans[t][1],w)-max(ans[t][2],w)+w
        if e<ans[tt][0]+ans[tt][1]-ans[tt][2]:
            ans[tt]=[ans[t][0]+w,min(ans[t][1],w),max(ans[t][2],w)]
        if not visited[tt]:
            visited[tt]=True
            dq.append(tt)
    print(ans,dq)
print(ans)
#n=int(sys.stdin.readline().strip())
#N1=int(NQ[0])
#N2=int(NQ[1])
#N3=int(NQ[1])

    
#for x,y in occupy:
#    l[x][y]="X"
#for ll in l:
#    print("".join(ll))

