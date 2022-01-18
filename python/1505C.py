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
AB=sys.stdin.readline().strip()
abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
d={}
for i in range(len(abc)):
    d[abc[i]]=i
    
F=True
l=[]
if len(AB)<=2:
    print("YES")
else:
    for i in range(2,len(AB)):
        a=d[AB[i-2]]
        b=d[AB[i-1]]
        c=d[AB[i]]
        if c!=(a+b)%26:
            F=False
            break
    if F:
        print("YES")
    else:
        print("NO")
    
