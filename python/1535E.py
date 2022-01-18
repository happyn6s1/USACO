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
Q,A,C=list(map(int,sys.stdin.readline().strip().split()))
d={}
d[0]=[C,A]
parent={}
parent[0]=-1

for i in range(Q):
    j=i+1
    t=list(map(int,sys.stdin.readline().strip().split()))
    if t[0]==1:
        _,p,a,c=t
        parent[j]=p
        d[j]=[c,a]
    else:
        _,v,w=t
        h=[]
        k=v
        while k>=0:
            h.append((d[k][0],d[k][1],k))
            k=parent[k]
        h.sort()
        cc=0
        ww=0
        #print(j,h,d)
        for c,a,k in h:
            if a==0:
                continue
            if a+ww>w:
                
                cc+=((w-ww)*c)
                d[k][1]-=(w-ww)
                ww=w
            else:
                ww+=a
                cc+=(a*c)
                d[k][1]=0
            if ww==w:
                break
        print(ww,cc)
        sys.stdout.flush()
