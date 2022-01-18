"""
ID: happyn61
LANG: PYTHON3
PROB: loan
"""
from itertools import product
import itertools
#from collections import defaultdict
import sys
import math
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
    ans=0
    s=sys.stdin.readline().strip()
    n=len(s)
    lo=0
    hi=0
    x=0 # number of matched
    y=0
    k=0
    flag=False
    t=[None,None]
    ans=n
    for hi in range(n):
        if s[hi]=="?":
            continue
        ss=int(s[hi])
        if not flag:
            flag=True
            t[hi%2]=ss
            t[(hi+1)%2]=1-ss
            x+=1
        else:
            if t[hi%2]==ss:
                x+=1
            else: #conflict
                kk=hi-lo
                #ans+=((kk-1)*kk)//2
                while x>0:
                    ans+=(hi-lo-1)
                    if s[lo]=="?":
                        lo+=1
                    else:
                        lo+=1
                        x-=1
                    
                #flag=False
                x=1
                t[hi%2]=ss
                t[(hi+1)%2]=1-ss
            
        #print(lo,hi,t,ans)
        
    kk=hi+1-lo
    ans+=((kk-1)*kk)//2
            
    print(ans)
