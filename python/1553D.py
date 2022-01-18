"""
ID: happyn61
LANG: PYTHON3
PROB: loan
"""
from itertools import product
import itertools
import math
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

#print(pp)
#d={"N":(0,1),"S":(0,-1),"W":(-1,0),"E":(1,0)}
for _ in range(K):
    s=sys.stdin.readline().strip()
    t=sys.stdin.readline().strip()
    def issub(m,n):
        if m==0:
            return True
        if n==0:
            return False
        #print(t,s,m,n)
        F1=False
        F2=False
        if t[m-1]==s[n-1]:
            F1=issub(m-1,n-1)
        if n>1:
            F2=issub(m,n-2)
        return F1 or F2
    def issub2(t,s):
        m=len(t)
        n=len(s)
        j=0
        i=0
        while j<m and i<n:
            #print(t,s,j,i)
            if t[j]==s[i]:
                j+=1
                i+=1
            else:
                i+=2
        return j==m
        #print(t,s,m,n)
        
    if issub2(t,s) or issub2(t,s[1:]):
        print("YES")
    else:
        print("NO")
