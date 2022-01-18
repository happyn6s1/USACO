"""
ID: happyn61
LANG: PYTHON3
PROB: threesum
"""
FN="threesum"
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
q=int(M)
l=fin.readline().strip().split()
d={}
for i in range(n):
    l[i]=int(l[i])
    if l[i] in d:
        d[l[i]].append(i)
    else:
        d[l[i]]=[i]
dl={k:[0 for j in range(n)]  for k in d}
for k in d:
    for t in d[k]:
        dl[k][t]+=1
    for i in range(n-2,-1,-1):
        dl[k][i]+=dl[k][i+1]
        
m=[[0 for j in range(n)] for i in range(n)]
print(dl)
for i in range(n-2):
    for j in range(i+1,n-1):
        if -l[i]-l[j] in d:
            
            m[i][k]+=dl[-l[i]-l[j]][j+1]
print(m)
for i in range(n):
    for j in range(n):
        if j>0:
            m[i][j]+=m[i][j-1]
for i in range(n-1,-1,-1):
    for j in range(n):
        if i<n-1:
            m[i][j]+=m[i+1][j]
#print(m,d)

for i in range(q):
    A,B=fin.readline().strip().split()
    a=int(A)
    b=int(B)
    
#print("--- %s seconds ---" % (time.time() - start_time))
#print(ans)
#print("--- %s seconds ---" % (time.time() - start_time))        
#print(ans)
#print(ans,"asda")
    print(m[a-1][b-1])
    fout.write(str(m[a-1][b-1])+"\n")            
fout.close()
