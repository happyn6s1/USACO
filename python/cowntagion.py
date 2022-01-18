"""
ID: happyn61
LANG: PYTHON3
PROB: loan
"""
from itertools import product
#from collections import defaultdict
import sys
import heapq
from collections import deque
MOD=1000000007
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

n=int(sys.stdin.readline().strip())
graph=[[]for i in range(n)]
for i in range(n-1):
    AB=sys.stdin.readline().strip().split()
    a=int(AB[0])-1
    b=int(AB[1])-1
    graph[a].append(b)
    graph[b].append(a)
dq=deque([])
s={0}
dq.append(0)
while dq:
    p=dq.popleft()
    k=0
    for q in graph[p]:
        if q not in s:
            k+=1
            s.add(q)
            dq.append(q)
    m=0
    o=1
    while o<k+1:
        o*=2
        m+=1
    
    ans+=(m+k)
    #print(m,p,graph,dq,k,ans)
print(ans)
#print(len(occupy))
