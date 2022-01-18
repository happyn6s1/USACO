"""
ID: happyn61
LANG: PYTHON3
PROB: helpcross
"""
FN="helpcross"
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
C,N=fin.readline().strip().split()
c=int(C)
n=int(N)

chicks=[]
for i in range(c):
    chicks.append(int(fin.readline().strip()))
chicks.sort()
cows=[]
for i in range(n):
    A,B=fin.readline().strip().split()
    a=int(A)
    b=int(B)
    cows.append((a,b))
cows.sort()
i=0
j=0
h=[]
cc=0
while i<c  :

    while j<n and cows[j][0]<=chicks[i]:
        heapq.heappush(h,(cows[j][1],cows[j][0]))
        j+=1
    #print(i,j,len(h))
    while h:
        b,a=heapq.heappop(h)
        if a<=chicks[i] and b>=chicks[i]:
            ans+=1
            
            break
    i+=1      
    #print(i,j,chicks,cows,ans)
print(ans)
#print(ans,"asda")
fout.write(str(ans)+"\n")            
fout.close()
