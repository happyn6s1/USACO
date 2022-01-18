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
pp=[]
for i in range(10):
    pp.append((-(i+1)//2,(i+1)//2))
pp.reverse()
#print(pp)
#d={"N":(0,1),"S":(0,-1),"W":(-1,0),"E":(1,0)}
for _ in range(K):
    s=sys.stdin.readline().strip()
    i=0
    m0=0
    m1=0
    for i in range(10):
        if i%2==0:
            
            if s[i]=="1":
                m0+=1
                m1+=1
            elif s[i]=="?":
                m1+=1
        else:
            if s[i]=="1":
                m0-=1
                m1-=1
            elif s[i]=="?":
                m0-=1
        if i<9:
            if m1+pp[i+1][0]>0 or m0+pp[i+1][1]<0:
                break
        else:
            break
    print(i+1)
