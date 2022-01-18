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

def ck(k,l):
    t=l[k]
    p=k
    ans=1
    for i in range(k-1,-1,-1):
        #print(l,p,i,t)
        if l[p]-l[i]>=t:
            ans+=1
            p=i
    #print("ret", l,k,ans)
    return ans
        
#d={"N":(0,1),"S":(0,-1),"W":(-1,0),"E":(1,0)}
for _ in range(K):
    ans=1
    n=int(sys.stdin.readline().strip())
    ll=list(map(int,sys.stdin.readline().strip().split()))
    ll.sort()
    lll=[]
    l=[]
    for t in ll:
        if t<=0:
            l.append(t)
        else:
            lll.append(t)
    if len(lll)==0:
        ans=n
    else:
        t=lll[0] #min
        if len(l)<1:
            ans=1
        
        else:
            F=False
            l.append(t)
            for i in range(1,len(l)):
                if l[i]-l[i-1]<t:
                    #print("a",l,lll,ll)
                    ans= len(l)-1
                    F=True
                    break
            if not F:
                ans=len(l)
    print(ans)
