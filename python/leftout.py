"""
ID: happyn61
LANG: PYTHON3
PROB: leftout
"""
FN="leftout"
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
N=int(fin.readline().strip())
#MN=fin.readline().strip().split()
#N=int(MN[0])
#M=int(MN[1])
    #print(ans)
ol=[]
ct=0
x=[]
y=[]
m=[["" for j in range(N)] for i in range(N)]
r=[[] for i in range(N)]
c=[[] for i in range(N)]
a=[]
b=[]
for i in range(N):
    lc=0
    rc=0
    s=fin.readline().strip()
    for j in range(N):
        m[i][j]=s[j]
        
        if s[j]=="L":
            lc+=1
        else:
            rc+=1
    r[i]=[lc,rc]
    if lc>1 and rc>1:
        a.append(i)
#print(mp)    
for j in range(N):
    lc=0
    rc=0
    for i in range(N):
        if m[i][j]=="L":
            lc+=1
        else:
            rc+=1
    c[j]=[lc,rc]
    if lc>1 and rc>1:
        b.append(j)
ans=[]
l=[]
print(a,b,r,c)
if N==2:
    ans=[1,1]
elif N==3:
    ans=[1,1]
elif len(a)>2 or len(b)>2:
    ans=[]
else:
     for i in a:
        for j in b:
            if m[i][j]=="L":
                ct=0
                for k in range(N):
                    if k==i:
                        
                        if r[k][0]-1>1 and r[k][0]+1>1:
                            ct+=1
                    else:
                        if r[k][0]>1 and r[k][0]>1:
                            ct+=1
                if ct<2:
                    for k in range(N):
                        if k==j:
                            
                            if c[k][0]-1>1 and c[k][0]+1>1:
                                ct+=1
                        else:
                            if c[k][0]>1 and c[k][0]>1:
                                ct+=1
                    
                
                    
            
#print(mp)
#print(ps)
print(ans)
#print(ans)
fout.write(str(ans)+"\n")            
fout.close()
