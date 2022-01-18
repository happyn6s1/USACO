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
MOD=1000000000007
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
#NK=sys.stdin.readline().strip().split()
K=int(sys.stdin.readline().strip())
#N=int(NK[0])
#K=int(NK[1])
#M=int(NK[2])
#ol=list(map(int,sys.stdin.readline().strip().split()))
#d={0:0,1:0}

x=0
y=0

#d={"N":(0,1),"S":(0,-1),"W":(-1,0),"E":(1,0)}
for _ in range(K):
    #a=int(sys.stdin.readline().strip())
    c,m,p,v=list(map(float,sys.stdin.readline().strip().split()))
    #print(c,m,p,v)
    stack=deque([(c,m,p,1,1)])
    ans=0
    while stack:
        c,m,p,kk,w=stack.popleft()
        #print(c,m,p,w)
        ans+=p*w*kk
        if (c-0.0000001)>0:
            k=c*kk
            if c<=v:
                #pp+=(c/2)
                #m+=(c/2)
                #c=0
                if (m-0.0000001)>0:
                    stack.append((0,m+c/2,p+c/2,k,w+1))
                else:
                    stack.append((0,0,p+c,k,w+1))

            else:
                if (m-0.0000001)>0:
                    stack.append((c-v,m+v/2,p+v/2,k,w+1))
                else:
                    stack.append((c-v,m,p+v,k,w+1))
        if (m-0.0000001)>0:
            k=m*kk
            if m<=v:
                if (c-0.0000001)>0:
                    stack.append((c+m/2,0,p+m/2,k,w+1))
                else:
                    stack.append((c,0,p+m,k,w+1))
                
            else:
                if (c-0.0000001)>0:
                    stack.append((c+v/2,m-v,p+v/2,k,w+1))
                else:
                    stack.append((c,m-v,p+v,k,w+1))
                
        #print(stack)
    print(ans)
