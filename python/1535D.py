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
ol=list(sys.stdin.readline().strip())
#d={0:0,1:0}
#ol.reverse()
k=2**K
l=[1 for i in range(k*2)]
for i in range(k-1):
    j=k-1-i
    if ol[i]=="?":
        l[j]=l[j*2]+l[j*2+1]
    elif ol[i]=="0":
        l[j]=l[j*2+1]
    else:
        l[j]=l[j*2]
Q=int(sys.stdin.readline().strip())
for i in range(Q):
    p,c=sys.stdin.readline().strip().split()
    p=int(p)
    j=k-p
    ol[p-1]=c
    while j>0:
        if ol[p-1]=="?":
            l[j]=l[j*2]+l[j*2+1]
        elif ol[p-1]=="0":
            l[j]=l[j*2+1]
        else:
            l[j]=l[j*2]
        j=j//2
        p=k-j
    print(l[1])
            
