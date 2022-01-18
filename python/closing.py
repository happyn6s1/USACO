"""
ID: happyn61
LANG: PYTHON3
PROB: closing
"""

#from collections import defaultdict

import heapq

fin = open ('closing.in', 'r')
fout = open ('closing.out', 'w')
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
N=int(NQ[0])
M=int(NQ[1])
parent=[i for i in range(N)]
rank=[0 for i in range(N)]
#n=int(fin.readline().strip())
ans=0
al=[]
s={i for i in range(N)}
b=[]
g=[[] for i in range(N)]
for i in range(M):
    NQ=fin.readline().strip().split()
    a=int(NQ[0])-1
    b=int(NQ[1])-1
    g[a].append(b)
    g[b].append(a)
def isConnected(start,n):
    visited=set()
    #print(n)
    stack=[start]
    while stack:
        p=stack.pop()
        #n-=1
        visited.add(p)
        for j in g[p]:
            if j in s and j not in visited:
                stack.append(j)
    #if start==0:
    #    print(visited,start,len(visited),n,s)
    if len(visited)==n:
        return True
    else:
        return False
q=[]
visit=set()
for i in range(N):
    q.append(int(fin.readline().strip())-1)

q.reverse()
ans=0
#print(q)
for i in range(N):
    k=q[i]
    ans+=1
    visit.add(k)
    for j in g[k]:
        if j in visit:
            #print(parent)
            if find(parent,k)!=find(parent,j):
                ans-=1
                union(parent,rank,k,j)
    #print(i,ans,parent)
    if ans==1:
        al.append(True)
    else:
        al.append(False)
al.reverse()
#print(al)
for k in al:
    if k:
        fout.write ("YES"+'\n')
    
    else:
        fout.write ("NO"+'\n')
        
'''
if isConnected(0,N):
    fout.write ("YES"+'\n')
    
else:
    fout.write ("NO"+'\n')

for i in range(N-1):
    s.remove(q[i])
    k=0
    for e in s:
        k=e
        break
    if isConnected(k,N-1-i):
        fout.write ("YES"+'\n')
    else:
        fout.write ("NO"+'\n')
'''

print(ans)


fout.close()
