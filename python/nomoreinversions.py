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
    n=int(AB[0])
    m=int(AB[1])
    l=[str(i+1) for i in range(m)]
    if 2*m-1-n==0:
        l.reverse()
        print(" ".join(l))
    else:
        ll=l[2*m-1-n:]
        ll.reverse()
        k=l[:2*m-1-n]+ll
        print(" ".join(k))
    #l=sys.stdin.readline().strip().split()
    #s1=sys.stdin.readline().strip()
    #s2=sys.stdin.readline().strip()
    
        #print(pre,post,ll,rr,m1,m2,pre[ll],post[n-1-rr],post[n-1-rr][2])
    #if F:
    #    print("yes")
    #else:
    #    print("no")
    #return True
    
#for x,y in occupy:
#    l[x][y]="X"
#for ll in l:
#    print("".join(ll))

