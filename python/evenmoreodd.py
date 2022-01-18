"""
ID: happyn61
LANG: PYTHON3
PROB: loan
"""
from itertools import product
import itertools
#from collections import defaultdict
import sys
import heapq
from collections import deque
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
K=int(sys.stdin.readline().strip())
l=sys.stdin.readline().strip().split()
o=0
e=0
for c in l:
    if int(c)%2==0:
        e+=1
    else:
        o+=1

if o>0 and e>0:
    ans+=(2*min(e,o))
    k=min(o,e)
    o-=k
    e-=k
#print(ans,o,e)
if o==0:
    ans+=1
    print(ans)
else:
    ans+=(o//3*2)
    if o%3==1:
        ans-=1
    elif o%3==2:
        ans+=1
    print(ans)
