"""
ID: happyn61
LANG: PYTHON3
PROB: loan
"""
import sys
# A Python program to print all 
# permutations using library function 
from itertools import permutations 
import functools
# Get all permutations of [1, 2, 3] 
perm = permutations([1, 2, 3]) 
  
# Print the obtained permutations 

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
        
def find(i):
    if parent[i] != i: 
        parent[i]=find(parent[i]) 
    return parent[i] 


def union(xx,yy): 
    x=find(xx)
    y=find(yy)
    if rank[x]>rank[y]:
        parent[y]=x
    elif rank[y]>rank[x]:
        parent[x]=y
    else:
        parent[y]=x
        rank[x]+=1
        
#fin = open ('loan.in', 'r')
#fout = open ('loan.out', 'w')
#print(dic["4734"])
n=int(sys.stdin.readline().strip())
#parent=[i for i in range(n*2)]
#rank=[0 for i in range(n*2)]


ans=0
#print(ans)

#NQ=sys.stdin.readline().strip().split()

l=[]
for tn in range(n):
    l.append(tuple(map(int,sys.stdin.readline().strip().split())))
#if n==3:
d={}
@functools.lru_cache(None)
def ar(A,B,C):
    #print(A,B,C,(A[1]-B[1])*C[0] + (B[0]-A[0])*C[1] + (A[0]*B[1]-B[0]*A[1]))
    return (A[1]-B[1])*C[0] + (B[0]-A[0])*C[1] + (A[0]*B[1]-B[0]*A[1])
'''
for a1 in range(n-2):
    for a2 in range(a1+1,n-1):
        for a3 in range(a2+1,n):
            A=[l[a1][0],l[a1][1]]
            B=[l[a2][0],l[a2][1]]
            C=[l[a3][0],l[a3][1]]
            d[(a1,a2,a3)]=(A[1]-B[1])*C[0] + (B[0]-A[0])*C[1] + (A[0]*B[1]-B[0]*A[1])
'''

ss=set()
pm=[]
pre=[None for i in range(n+1)]
def isSafe(col,i,pre):
    if col==3:
        pre[col]=pm[:3]
    if col<3:
        return True
    #print(pre)
    #print(col,pm,col,pre)
    tl=[i]+pre[col]
    
    tl.sort()
    F=True
    k=0
    A=B=C=D=1
        #print(i,j,pre,tl)
    if ar(l[tl[0]],l[tl[1]],l[tl[2]])<0:
            
        k+=1
        D=-1
    if ar(l[tl[0]],l[tl[1]],l[tl[3]])<0:
        k+=1
        C=-1
    if ar(l[tl[1]],l[tl[2]],l[tl[3]])<0:
        k+=1
        A=-1
    if ar(l[tl[2]],l[tl[0]],l[tl[3]])<0:
        k+=1
        B=-1
        
    if k%2==1:
        #print(tl,i,k)
        F=False
        
    else:
        if k==0 or k==4:
            pre[col+1]=[tl[0],tl[1],tl[2]]
                
                
        elif A*B==1:
            pre[col+1]=[tl[0],tl[1],tl[3]]
                
        elif C*B==1:
            pre[col+1]=[tl[1],tl[2],tl[3]]
                
        else:
            pre[col+1]=[tl[0],tl[2],tl[3]]
    return F
            #print(tl,pre)
def tr(col,res):
    r=False
    #print(col)
    if col>=n:
        res[0]+=1
        return True
    for i in range(n):
        if i not in ss:

            if isSafe(col,i,pre):
                #print(col,i,pm)
                ss.add(i)
                pm.append(i)
                r=tr(col+1,res)
                pm.pop()
                ss.remove(i)
    return r
al=[0]
tr(0,al)
print(al[0] %MOD)
