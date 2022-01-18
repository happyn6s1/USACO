"""
ID: happyn61
LANG: PYTHON3
PROB: loan
"""
import sys
'''
from itertools import product
import itertools
import functools
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
'''
#NK=sys.stdin.readline().strip().split()
K=int(sys.stdin.readline().strip())
#N=int(NK[0])
#K=int(NK[1])
#M=int(NK[2])
ol=list(map(int,sys.stdin.readline().strip().split()))
#d={0:0,1:0}
#MAX=MOD
ol.sort()
#ans=MOD
'''
@functools.lru_cache(None)
def dpf(i,j):
    if i==j:
        return 0
    return ol[j]-ol[i]+min(dpf(i+1,j),dpf(i,j-1))
'''

dp=[[0]*K for i in range(K)]
for j in range(1,K): #offset
    for i in range(0,K-j): #row
        k=i+j
        dp[i][k]=min(dp[i+1][k],dp[i][k-1])+ol[k]-ol[i]
        
print(dp[0][-1])
#print(dp)
#print(dpf(0,K-1))
#print(ans)
