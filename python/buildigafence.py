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

for j in range(n):
        
    AB=sys.stdin.readline().strip().split()
    a=int(AB[0])
    k=int(AB[1])
    la=sys.stdin.readline().strip().split()

    lo=int(la[0])
    hi=int(la[0])
    F=True
    #print(la)
    for i in range(1,len(la)):
        aa=int(la[i])
        lo=max(aa,lo-(k-1))
        hi=min(aa+(k-1),hi+(k-1))
        if lo>hi:
            F=False
            break
        #print(i,lo,hi,la)
    if lo>int(la[-1]):
        F=False
    if F:
        print("yes")
    else:
        print("no")
    #return True
    
#for x,y in occupy:
#    l[x][y]="X"
#for ll in l:
#    print("".join(ll))

