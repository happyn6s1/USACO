"""
ID: happyn61
LANG: PYTHON3
PROB: loan
"""
from itertools import product
#from collections import defaultdict
import sys
import heapq
MOD=1000000007
#fin = open ('loan.in', 'r')
#fout = open ('loan.out', 'w')
#print(dic["4734"])
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
STR=sys.stdin.readline().strip()
#n=int(fin.readline().strip())
l=[]
for c in STR:
    l.append(c)
#AGCT
n=len(l)
for kk in product('AGCT', repeat=n):
    sp=[0]
    k="".join(kk)
    for i in range(1,n):
        if k[i-1]==k[i]:
            sp.append(i)
    #print(sp)
    conv=[]
    sp.append(n)
    if len(sp)>2:
        for j in range(1,len(sp)):
            t=k[sp[j-1]:sp[j]]
            #print(t)
            
            conv.append(t[::-1])
    else:
        conv=k
    conv="".join(conv)
    #print(k,conv)
    F=True
    for i in range(n):
        if l[i]!="?" and l[i]!=conv[i]:
            F=False
            break
    if F:
        ans+=1
    
d={"A":0,"G":1,"C":2,"T":3}

print(ans)
#print(len(occupy))
