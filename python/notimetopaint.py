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
NK=sys.stdin.readline().strip().split()
N=int(NK[0])
Q=int(NK[1])
#M=int(NK[2])
S=sys.stdin.readline().strip()
l=list(S)
a1=[0]
a2=[0]

stack=[]
m=0
for i in range(N):
    while stack and stack[-1]>l[i]:
        stack.pop()
    if stack and stack[-1]==l[i]:
        a1.append(m)
    else:
        m+=1
        a1.append(m)
        stack.append(l[i])
l.reverse()
stack=[]
m=0
for i in range(N):
    while stack and stack[-1]>l[i]:
        stack.pop()
    if stack and stack[-1]==l[i]:
        a2.append(m)
    else:
        m+=1
        a2.append(m)
        stack.append(l[i])
a2.reverse()
for i in range(Q):
    AB=sys.stdin.readline().strip().split()
    x=int(AB[0])
    y=int(AB[1])
    #print(a1,a2)
    print(a1[x-1]+a2[y])
#print(a2)

#print(ans)
#print(len(occupy))
