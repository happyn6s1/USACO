"""
ID: happyn61
LANG: PYTHON3
PROB: mootube
"""

#from collections import defaultdict

import heapq

fin = open ('mootube.in', 'r')
fout = open ('mootube.out', 'w')
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
n=int(NQ[0])
q=int(NQ[1])
l=[]
ans=[]
graph=[[]for i in range(n)]
for i in range(n-1):
    XY=fin.readline().strip().split()
    x=int(XY[0])-1
    y=int(XY[1])-1
    z=int(XY[2])
    graph[x].append((y,z))
    graph[y].append((x,z))
for i in range(q):
    XY=fin.readline().strip().split()
    x=int(XY[0])
    y=int(XY[1])-1
    stack=[y]
    s=set()
    while stack:
        p=stack.pop()
        s.add(p)
        for e in graph[p]:
            if e[0] not in s and e[1]>=x:
                stack.append(e[0])
    k=len(s)
    #print(parent,y)
    ans.append(k-1)

#print(ans)
for i in range(q):
    fout.write (str(ans[i])+'\n')
fout.close()
