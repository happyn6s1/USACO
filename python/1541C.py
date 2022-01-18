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
e=[[] for i in range(K)]
for _ in range(K-1):
    #n=int(sys.stdin.readline().strip())
    a,b=list(map(int,sys.stdin.readline().strip().split()))
    e[a-1].append(b-1)
    e[b-1].append(a-1)
#print(e)

def inmid(i,j,k):
    stack=[]
    ss=set()
    #stack.append(i)
    visited=[False for ii in range(K)]
    st=set()
    def dfs(i,j):
        stack.append(i)
        if i==j:
            for t in stack:
                st.add(t)
            #print(stack,st)
            return True
        visited[i]=True
        for jj in e[i]:
            if visited[jj]==False:
                if dfs(jj,j):
                    return True
        stack.pop()
    dfs(i,j)
    #print(i,j,k,st)
    #print(k in st,k,st)
    return k in st
def iorj(i,j,k):
    stack=[]
    ss=set()
    stack.append(k)
    visited=[False for ii in range(K)]
    visited[k]=True
    while stack:
        p=stack.pop()
        ss.add(p)
        if p==i or p==j:
            break
            if not visited[q]:
                stack.append(q)
                visited[q]=True
    if p==i:
        return True
    else:
        return False
for i in range(K-1):
    for j in range(i+1,K):
        for k in range(K):
            if k==i or k==j:
                continue
            
            if inmid(i,j,k):
                ans+=3
            else:
                if not iorj(i,j,k):
                    ans+=2
            print(i,j,k,ans)
#print(ans)
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
m=K-2                
M=10**9+7
b=K*2
a=ans
c=math.gcd(a,b)
a=a//c
b=b//c
print(a,b,ans,K*2)
print(modinv(b,M)*a % M,modinv(K*2,M)*ans % M)

