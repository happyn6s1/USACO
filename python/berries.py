"""
ID: happyn61
LANG: PYTHON3
PROB: berries
"""

#from collections import defaultdict
import sys
import heapq

fin = open ('berries.in', 'r')
fout = open ('berries.out', 'w')
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
        
NQ=fin.readline().strip().split()
#n=int(fin.readline().strip())
N=int(NQ[0])
K=int(NQ[1])
bl=fin.readline().strip().split()
m=0
h=[]
for i in bl:
    heapq.heappush(h,-int(i))
m=-h[0]
ans=0

print(N,K,m)
k=K//2
for j in range(m):
    c=j+1
    hh=h.copy()
    for i in range(k):
        if not hh:
            break
        p=-heapq.heappop(hh)
        if p>c:
            heapq.heappush(hh,c-p)
    r=0
    for i in range(k):
        if not hh:
            break
        p=-heapq.heappop(hh)
        if p>c:
            heapq.heappush(hh,c-p)
            r+=c
        else:
            r+=p
    ans=max(r,ans)
print(ans)

fout.write (str(ans)+'\n')
fout.close()
