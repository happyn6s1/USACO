"""
ID: happyn61
LANG: PYTHON3
PROB: moop
"""

#from collections import defaultdict

import heapq

fin = open ('moop.in', 'r')
fout = open ('moop.out', 'w')
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
        
N=fin.readline().strip()
n=int(N)
l=[]
ans=0
parent=[i for i in range(n)]
rank=[0 for i in range(n)]
for i in range(n):
    XY=fin.readline().strip().split()
    x=int(XY[0])
    y=int(XY[1])
    l.append((x,y))
for i in range(n-1):
    for j in range(i+1,n):
        if l[i][0]<=l[j][0] and l[i][1]<=l[j][1] or l[i][0]>=l[j][0] and l[i][1]>=l[j][1]:
            #print(i,j)
            if find(parent,i) !=find(parent,j):
                union(parent,rank,i,j)

s=set()
for i in range(n):
    s.add(find(parent,i))
ans=len(s)
print(ans)
fout.write (str(ans)+'\n')
fout.close()
