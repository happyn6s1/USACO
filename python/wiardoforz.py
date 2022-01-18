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
#N=int(NQ[0])
#D=int(NQ[1])
for i in range(n):
    d={}
    a=9
    b=-1
    m=int(sys.stdin.readline().strip())
    ans=[]
    for i in range(m):
        #print(i,a,b)
        ans.append(str(a))
        #ans=ans*10+a
        a=(a+b)%10
        if a==8 and b==-1:
            b=1
        #print(ans,a,b)
    print("".join(ans))
#for x,y in occupy:
#    l[x][y]="X"
#for ll in l:
#    print("".join(ll))

