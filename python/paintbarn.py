"""
ID: happyn61
LANG: PYTHON3
PROB: paintbarn
"""
FN="paintbarn"
import collections,heapq
import sys
INF=999999
AL="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
al="abcdefghijklmnopqrstuvwxyz"
cost={}
visited=set()
hcost=[]
d={}

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
BIG=1000
fin = open (FN+'.in', 'r')
fout = open (FN+'.out', 'w')
#N=int(fin.readline().strip())
MN=fin.readline().strip().split()
N=int(MN[0])
M=int(MN[1])
    #print(ans)
ol=[]
ct=0
x=[]
y=[]
mp=[[0 for j in range(BIG)] for i in range(BIG)]
for i in range(N):
    pt=fin.readline().strip().split()
    ol.append((int(pt[0]),int(pt[1]),int(pt[2]),int(pt[3])))
    mp[ol[i][0]][ol[i][1]]+=1
    mp[ol[i][0]][ol[i][3]]-=1
    mp[ol[i][2]][ol[i][1]]-=1
    mp[ol[i][2]][ol[i][3]]+=1
#print(mp)    
for i in range(BIG):
    for j in range(BIG-1):
        if i>0:
            mp[i][j]+=mp[i-1][j]
        if j>0:
            mp[i][j]+=mp[i][j-1]
        if i>0 and j>0:
            mp[i][j]-=mp[i-1][j-1]
        if mp[i][j]==M:
            ans+=1
            
#print(mp)
#print(ps)
print(ans)
#print(ans)
fout.write(str(ans)+"\n")            
fout.close()
