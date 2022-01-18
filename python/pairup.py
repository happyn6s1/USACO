"""
ID: happyn61
LANG: PYTHON3
PROB: pairup
"""
FN="pairup"
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
#C,N=fin.readline().strip().split()
N=fin.readline().strip()
n=int(N)
cows=[]
lo=0
hi=0
m=0
for i in range(n):
    A,B=fin.readline().strip().split()
    a=int(A)
    b=int(B)
    hi=max(hi,b)
    cows.append([b,a])
    lo+=b
    m+=a
lo=lo*2//m
cows.sort()
cp=[list(tuple(n)) for n in cows]
hi=hi*2
#print(hi,lo)

def check():
    i=0
    ans=0
    j=len(cows)-1
    while i<=j:
        if i==j:
            return max(ans,cows[i][0]*2)
        else:
            ans=max(ans,cows[i][0]+cows[j][0])
            if cows[i][1]==cows[j][1]:
                i+=1
                j-=1
            elif cows[i][1]>cows[j][1]:
                cows[i][1]-=cows[j][1]
                j-=1
            else:
                cows[j][1]-=cows[i][1]
                i+=1
    return ans

ans=check()
lo=hi+1
while lo<=hi:
    mi=(lo+hi)//2
    for i in range(len(cows)):
        cows[i]=list(tuple(cp[i]))
    #print(cows[0])
    if check(mi):
        #print(mi)
        ans=mi
        hi=mi-1
    else:
        lo=mi+1
        
    
    
    #print(i,j,chicks,cows,ans)
print(ans)
#print(ans,"asda")
fout.write(str(ans)+"\n")            
fout.close()
