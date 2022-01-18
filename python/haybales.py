"""
ID: happyn61
LANG: PYTHON3
PROB: haybales
"""
FN="haybales"
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
def fit(n,ol,limit):
    k=0
    i=0
    F=True
    p=-1
    while i<len(ol):
        if F:
            p=ol[i][0]
            F=False
            k+=1
            
        else:
            if p+n<=ol[i][1]:
                #print(ol[i],p,n)
                ps=max(p+n,ol[i][0])
                m=(ol[i][1]-ps)//n+1
                p=ps+m*n-n
                k+=m
                i+=1
            else:
                i+=1
        if k>=limit:
            #print(n)
            return True
    return False
                
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
rl=fin.readline().strip().split()
l=[]
sm=[0]
for i in rl:
    l.append(int(i))
    
l.sort()

for i in l:
    sm.append(sm[-1]+1)
    
#print(sm)
def findl(n):
    lo=0
    hi=len(l)-1
    rt=0
    while lo<=hi:
        mi=(lo+hi)//2
        #print(n,mi,"adf")
        if l[mi]<=n:
            rt=mi+1
            lo=mi+1
        else:
            hi=mi-1
    #print(n,rt)
    return rt
for i in range(M):
    ab=fin.readline().strip().split()
    a=int(ab[0])
    b=int(ab[1])
    ans=sm[findl(b)-findl(a-1)]
    #print(ans)
    fout.write(str(ans)+"\n")            
fout.close()
