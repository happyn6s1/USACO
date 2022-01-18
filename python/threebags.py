"""
ID: happyn61
LANG: PYTHON3
PROB: loan
"""

#from collections import defaultdict
import sys
import heapq
from collections import deque

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

NQ=sys.stdin.readline().strip().split()

#n=int(sys.stdin.readline().strip())
N1=int(NQ[0])
N2=int(NQ[1])
N3=int(NQ[1])

l=[]
ll=[[] for i in range(3)]
for j in range(3):
    L=sys.stdin.readline().strip().split()
    
    for t in L:
        ll[j].append(int(t))
        l.append(int(t))
l.sort()
ll[0].sort()
ll[1].sort()
ll[2].sort()
lll=[]
for i in range(3):
    lll.append(ll[i][0])
lll.sort()
a=sum(lll[:2])

for i in range(3):
    a=min(a,sum(ll[i]))
print(sum(l)-a*2)
#for x,y in occupy:
#    l[x][y]="X"
#for ll in l:
#    print("".join(ll))

