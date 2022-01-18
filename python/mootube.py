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
    x=int(XY[0])
    y=int(XY[1])
    z=int(XY[2])
    
    l.append((x-1,y-1,z))
for i in range(q):
    XY=fin.readline().strip().split()
    x=int(XY[0])
    y=int(XY[1])
    parent=[i for i in range(n)]
    rank=[0 for i in range(n)]
    for t in l:
        #print(i,t,x)
        if t[2]>=x:
            #print(i,j)
            if find(parent,t[0]) !=find(parent,t[1]):
                union(parent,rank,t[0],t[1])
    k=0
    #print(parent,y)
    for i in range(n):
        if find(parent,i)==find(parent,y-1):
            k+=1
    ans.append(k-1)

#print(ans)
for i in range(q):
    fout.write (str(ans[i])+'\n')
fout.close()
