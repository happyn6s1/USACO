"""
ID: happyn61
LANG: PYTHON3
PROB: cownomics
"""
FN="cownomics"
import collections,heapq,time
from itertools import combinations 
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
N,M=fin.readline().strip().split()
#N=fin.readline().strip()
n=int(N)
m=int(M)
start_time = time.time()
m1=[["" for j in range(m)] for i in range(n)]
m2=[["" for j in range(m)] for i in range(n)]

for i in range(n):
    s=fin.readline().strip()
    #print(s)
    for j in range(m):
        m1[i][j]=s[j]
for i in range(n):
    s=fin.readline().strip()
    for j in range(m):
        m2[i][j]=s[j]
#print(m1,m2)
comb = combinations([i for i in range(m)], 3)

print("--- %s seconds ---" % (time.time() - start_time))
for c in list(comb):
    #print(c)
    s1=set()
    F=True
    for i in range(n):
        s1.add((m1[i][c[0]],m1[i][c[1]],m1[i][c[2]]))
    for i in range(n):
        if (m2[i][c[0]],m2[i][c[1]],m2[i][c[2]]) in s1:
            F=False
            break
    if F:
        ans+=1
#print(ans)
print("--- %s seconds ---" % (time.time() - start_time))        
#print(ans)
#print(ans,"asda")
fout.write(str(ans)+"\n")            
fout.close()
