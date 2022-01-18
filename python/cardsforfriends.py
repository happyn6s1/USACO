"""
ID: happyn61
LANG: PYTHON3
PROB: loan
"""

#from collections import defaultdict
import sys
import heapq

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
#N=int(NQ[0])
#D=int(NQ[1])
for i in range(n):
    K=sys.stdin.readline().strip().split()
    w=int(K[0])
    h=int(K[1])
    m=int(K[2])
    F=True
    a=1
    while w%2==0:
        a*=2
        w=w//2
    while h%2==0:
        a*=2
        h=h//2
    F=(a>=m)
    if F:
        print("YES")
    else:
        print("NO")
#for x,y in occupy:
#    l[x][y]="X"
#for ll in l:
#    print("".join(ll))

