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
K=int(NK[1])
M=int(NK[2])
ans=[{i} for i in range(N)]
aset=[{i} for i in range(N)]
ab=[i for i in range(N)]
p=[i for i in range(N)]
k=[]
for i in range(K):
    A,B=sys.stdin.readline().strip().split()
    A=int(A)-1
    B=int(B)-1

    k.append((A,B))
#print(k)
for i in range(K):
    kk=i
    A=k[kk][0]
    B=k[kk][1]
    t=p[B]
    p[B]=p[A]
    p[A]=t
    aset[p[A]].add(A)
    aset[p[B]].add(B)
    ab[p[A]]=A
    ab[p[B]]=B
#print(p)
steps=[-1 for i in range(N)]
v=[False for i in range(N)]

for i in range(N):
    if steps[i]>-1:
        continue
    ss={i}
    head=i
    node=p[i]
    while node!=i:
        ss.add(node)
        node=p[node]
    for tt in ss:
        steps[tt]=len(ss)
#print(steps)
#print(aset,steps,ans)
p=[i for i in range(N)]
aaa=[[{i}] for i in range(N)]
aa=[1 for i in range(N)]
for i in range(K):
    kk=i%K
    A=k[kk][0]
    B=k[kk][1]
    t=p[B]
    p[B]=p[A]
    p[A]=t
    ans[p[A]].add(A)
    ans[p[B]].add(B)
    
    #print(A,B,p,ans)
    for j in range(N):
        aaa[j].append(ans[j].copy())
    #print(aaa)
#print(aset,steps,ans,aaa)
#for i in range(max(steps)):
pp=[1 for i in range(N)]
for i in range(N):
    pp[p[i]]=i
#print(pp)
for i in range(N):
    if M>=steps[i]*K:
        steps[i]    
    else:
        
        #aa[i]=aaa[i][M]
        step=M//K
        rest=M%K
        returns=set()
        cur=i
        #print(step,rest,aaa,aaa[cur],"asdfa")
        while step>0:
            step-=1
            returns=returns.union(aaa[cur][-1])
            cur=pp[cur]
        #print("now",i,cur,aaa[cur],returns)
        if rest>0:
            returns=returns.union(aaa[cur][rest])
        aa[i]=len(returns)
for i in range(N):
    print(aa[i])
#print(ans)
#print(len(occupy))
