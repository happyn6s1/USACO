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
AB=sys.stdin.readline().strip().split()
N=int(AB[0])
M=int(AB[1])
t=[]
while N>0:
    
    t.append(N%M)
    #print(t,N,N%M)
    N=N//M
#print(t)
F1=True
F2=True
if len(t)>1:
    for i in range(1,len(t)):
        if t[i]>=t[i-1]:
            F1=False
        if t[i]<=t[i-1]:
            F2=False
            
if F1 or F2:
    print("YES")
else:
    print("NO")
    
