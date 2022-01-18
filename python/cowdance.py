"""
ID: happyn61
LANG: PYTHON3
PROB: cowdance
"""
FN="cowdance"
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
#rl=fin.readline().strip().split()
l=[]
sm=[0]
for i in range(N):
    dd=int(fin.readline().strip())
    l.append(dd)
    

    
#print(sm)
def check(n):
    #ll=[0 for i in range(n)]
    hp=[]
    for i in range(n):
        hp.append((0,i))
    m=0
    for n in l:
        a,b=heapq.heappop(hp)
        if a+n<=M:
            heapq.heappush(hp,(a+n,b))
        else:
            return False
    return True
        
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
lo=1
hi=N
ans=hi
while lo<=hi:
    mi=(lo+hi)//2
    if check(mi):
        ans=mi
        hi=mi-1
    else:
        lo=mi+1
print(ans)
fout.write(str(ans)+"\n")            
fout.close()
