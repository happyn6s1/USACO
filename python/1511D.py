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
#K=int(sys.stdin.readline().strip())
#N=int(NK[0])
#K=int(NK[1])
#M=int(NK[2])
#ol=list(map(int,sys.stdin.readline().strip().split()))
#d={0:0,1:0}

x=0
y=0
n,k=list(map(int,sys.stdin.readline().strip().split()))
a2z="abcdefghijklmnopqrstuvwxyz"
pairs=set()
d={}
x="a"
ans=[]
l=["","aa"]

for i in range(1,k):
    j=i
    t=[]
    t.append(a2z[j])
    t.append(a2z[j])
    for kk in range(j-1):
        t.append(a2z[kk])
        t.append(a2z[j])
    t.append(l[j])
    t.append(a2z[j])
    l.append("".join(t))
k=k*k
ans.append(l[-1][1:]*(n//k))
if k==1:
    kk=0
else:
    kk=n%k
    ans.append(l[-1][:kk])
print("".join(ans))
