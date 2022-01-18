"""
ID: happyn61
LANG: PYTHON3
PROB: hps
"""
FN="hps"
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
N=int(fin.readline().strip())
P1=[0 for i in range(N)]
H1=[0 for i in range(N)]
S1=[0 for i in range(N)]
P2=[0 for i in range(N)]
H2=[0 for i in range(N)]
S2=[0 for i in range(N)]
l=[]
for i in range(N):
    c=fin.readline().strip()
    if i>0:
        P1[i]=P1[i-1]
        H1[i]=H1[i-1]
        S1[i]=S1[i-1]
    if c=="P":
        if i==0:
            P1[i]=1
        else:
            P1[i]=P1[i-1]+1
            
    if c=="H":
        if i==0:
            H1[i]=1
        else:
            H1[i]=H1[i-1]+1

    if c=="S":
        if i==0:
            S1[i]=1
        else:
            S1[i]=S1[i-1]+1
    l.append(c)

for i in range(N-1,-1,-1):
    c=l[i]
    if i<N-1:
        P2[i]=P2[i+1]
        H2[i]=H2[i+1]
        S2[i]=S2[i+1]
    if c=="P":
        if i==N-1:
            P2[i]=1
        else:
            P2[i]=P2[i+1]+1
            
    if c=="H":
        if i==N-1:
            H2[i]=1
        else:
            H2[i]=H2[i+1]+1

    if c=="S":
        if i==N-1:
            S2[i]=1
        else:
            S2[i]=S2[i+1]+1    

ans=0
ans=max(ans,P1[-1])
ans=max(ans,S1[-1])
ans=max(ans,H1[-1])
ans=max(ans,P2[0])
ans=max(ans,S2[0])
ans=max(ans,H2[0])
#print(P1,P2,S1,S2,H1,H2)
for i in range(1,N):
    a=0
    b=0
    a=max(a,P1[i-1])
    a=max(a,H1[i-1])
    a=max(a,S1[i-1])
    b=max(b,P2[i])
    b=max(b,H2[i])
    b=max(b,S2[i])
    ans=max(a+b,ans)
    
#MN=fin.readline().strip().split()
#N=int(MN[0])
#M=int(MN[1])
    #print(ans)
    

    
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

print(ans)
fout.write(str(ans)+"\n")            
fout.close()
