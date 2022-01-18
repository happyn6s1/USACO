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
N=int(sys.stdin.readline().strip())
#N=int(NK[0])
#Q=int(NK[1])
#M=int(NK[2])
#S=sys.stdin.readline().strip()
#l=list(S)
a1=[0]
a2=[0]

stack=[]
m=[]
for i in range(N):
    l=list(map(int,sys.stdin.readline().strip().split()))
    m.append(l)
#print(m)
w0=[]
w1=[]
for j in range(N):
    a=b=0
    for i in range(N):
        if i%2==0:
            a+=m[i][j]
        else:
            b+=m[i][j]
    w0.append(a)
    w1.append(b)
for i in range(N):
    ans+=max(w0[i],w1[i])
ans2=ans
ans=0
w0=[]
w1=[]
for i in range(N):
    a=b=0
    for j in range(N):
        if j%2==0:
            a+=m[i][j]
        else:
            b+=m[i][j]
    w0.append(a)
    w1.append(b)
for i in range(N):
    ans+=max(w0[i],w1[i])
print(max(ans,ans2))
#print(a2)

#print(ans)
#print(len(occupy))
