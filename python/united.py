"""
ID: happyn61
LANG: PYTHON3
PROB: loan
"""
import sys
'''
from collections import defaultdict

import heapq
import math
from collections import deque
MOD=1000000007
def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]
def factor(n,l,d):
    F=False
    for p in l:
        if n%p==0:
            if p in d:
                d[p]+=1
            else:
                d[p]=1
            F=True
            break
    if F:
        factor(n//p,l,d)
            
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
'''
ans=0

#NQ=sys.stdin.readline().strip().split()

n=int(sys.stdin.readline().strip())
l=list(map(int,sys.stdin.readline().strip().split()))
def getsum(BITTree,i): 
    s = 0 #initialize result 

    # index in BITree[] is 1 more than the index in arr[] 
    i = i+1

    # Traverse ancestors of BITree[index] 
    while i > 0: 

        # Add current element of BITree to sum 
        s += BITTree[i] 

        # Move index to parent node in getSum View 
        i -= i & (-i) 
    return s 

# Updates a node in Binary Index Tree (BITree) at given index 
# in BITree. The given value 'val' is added to BITree[i] and 
# all of its ancestors in tree. 
def updatebit(BITTree , n , i ,v): 

    # index in BITree[] is 1 more than the index in arr[] 
    i += 1

    # Traverse all ancestors and add 'val' 
    while i <= n: 

        # Add 'val' to current node of BI Tree 
        BITTree[i] += v 

        # Update index to that of parent in update View 
        i += i & (-i) 


# Constructs and returns a Binary Indexed Tree for given 
# array of size n. 
def construct(arr, n): 

    # Create and initialize BITree[] as 0 
    BITTree = [0]*(n+1) 

    # Store the actual values in BITree[] using update() 
    for i in range(n): 
        updatebit(BITTree, n, i, arr[i]) 

    # Uncomment below lines to see contents of BITree[] 
    #for i in range(1,n+1): 
    #     print BITTree[i], 
    return BITTree 

d={}
post={}
nxt=[None for i in range(n)]
for i in range(len(l)-1,-1,-1):
    if l[i] not in d:
        d[l[i]]=i
        
    else:
        nxt[i]=d[l[i]]
        d[l[i]]=i
freq=[1 for i in range(n)]
ans=0
#print(post)
for i in range(n):
    if nxt[i]:
        freq[nxt[i]]=0
#print(freq)
BITTree = construct(freq,len(freq)) 
for i in range(n-1):
    k=l[i]
    v=getsum(BITTree,i)
    if not nxt[i]:
        ans+=getsum(BITTree,n-1)-v
    else:      
        ans+=getsum(BITTree,nxt[i]-1)-v
        updatebit(BITTree,n,nxt[i],1)
    #print(ans,freq,post)
#print(d,freq)
print(ans)
