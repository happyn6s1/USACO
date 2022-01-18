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

#NQ=sys.stdin.readline().strip().split()

n=int(sys.stdin.readline().strip())
#N1=int(NQ[0])
#N2=int(NQ[1])
#N3=int(NQ[1])

for i in range(n):
    a=int(sys.stdin.readline().strip())
    la=sys.stdin.readline().strip().split()
    b=int(sys.stdin.readline().strip())
    lb=sys.stdin.readline().strip().split()
    k1=0
    s1=0
    for n in la:
        s1+=int(n)
        k1=max(k1,s1)
    k2=0
    s1=0
    for n in lb:
        s1+=int(n)
        k2=max(k2,s1)
    print(k1+k2)
    #return True
    
#for x,y in occupy:
#    l[x][y]="X"
#for ll in l:
#    print("".join(ll))

