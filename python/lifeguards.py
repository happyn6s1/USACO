"""
ID: happyn61
LANG: PYTHON3
PROB: lifeguards
"""
FN="lifeguards"
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
#N,M=fin.readline().strip().split()
N=fin.readline().strip()
n=int(N)
l=[]
v=[0 for i in range(n)]
for i in range(n):
    AB=fin.readline().strip().split()
    a=int(AB[0])
    b=int(AB[1])
    l.append([a,1,i])
    l.append([b,-1,i])
l.sort()

#print(l)
s=set()
s.add(l[0][2])
for i in range(len(l)):
    if i>0:
        #print(l,i,s)
        if l[i-1][1]>0:
            ans+=(l[i][0]-l[i-1][0])
        if l[i-1][1]==1:
            v[list(s)[0]]+=(l[i][0]-l[i-1][0])
            
        if l[i][1]>0:
            s.add(l[i][2])
        else:
            s.remove(l[i][2])
        l[i][1]+=l[i-1][1]
        
#print(ans-min(v))
ans-=min(v)
#print("--- %s seconds ---" % (time.time() - start_time))
#print(ans)
#print("--- %s seconds ---" % (time.time() - start_time))        
#print(ans)
#print(ans,"asda")
fout.write(str(ans)+"\n")            
fout.close()
