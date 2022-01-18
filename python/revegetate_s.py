"""
ID: happyn61
LANG: PYTHON3
PROB: revegetate
"""
FN="revegetate"
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
print(M,N)
parent=[i for i in range(N+1)]
rank=[0 for i in range(N+1)]
rel=[[] for i in range(N+1)]
val=[1 for i in range(N+1)]
#org=[]
for i in range(M):
    pt=fin.readline().strip().split()
    a=int(pt[1])
    b=int(pt[2])
    if pt[0]=="D":
        rel[a].append((b,-1))
        rel[b].append((a,-1))
    else:
        rel[a].append((b,1))
        rel[b].append((a,1))
    #org.append((a,b,pt[0]))
    if find(parent,a) != find(parent,b):
        union(parent,rank,a,b)
s=set()
for i in range(1,N+1):
    if find(parent,i) not in s:
        s.add(find(parent,i))
ans=len(s)
F=False
for k in s:
    stack=[(k,k,1)]
    ss=set()
    while stack:
        kk=stack.pop()
        
            
        val[kk[1]]=kk[2]*val[kk[0]]
        ss.add(kk[1])
        #print(ss,kk)
        for t in rel[kk[1]]:
            if t[0] not in ss:
                stack.append((kk[1],t[0],t[1]))

for i in range(1,N+1):
    for r in rel[i]:
        if val[i]*val[r[0]]!=r[1]:
            print(r,i,val[i],val[r[0]])
            F=True
            break
    if F:
        break

if F:
    fout.write("0"+"\n")            
    fout.close()
else:
    #print(ans)
    #print(ans)
    fout.write("1"+"0"*ans+"\n")            
    fout.close()
