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
import math
from collections import deque
MOD=10**9+7
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
def factorof(div,n):
	if (n%div) == 0:
		return True
	else:
		return False
		
def minfactor(n):
	for i in range(2,n+1):
		if(factorof(i,n)):
			return i
			
def factoring(n):
	fct=[]
	while n>1:
		f=minfactor(n)
		n=n//f
		match=False
		for i in range(0,len(fct)):
			if fct[i][0] == f:
				fct[i][1]=fct[i][1]+1
				match=True
				break
			if fct[i][0]>f:
				break
		if not match:
				fct.append([f,1])
	return fct	    
ans=0
#NK=sys.stdin.readline().strip().split()
K=int(sys.stdin.readline().strip())
#N=int(NK[0])
#K=int(NK[1])
#M=int(NK[2])
#ol=list(map(int,sys.stdin.readline().strip().split()))
#d={0:0,1:0}
from math import gcd as bltin_gcd
def coprime2(a, b):
    return bltin_gcd(a, b) == 1
x=0
y=0
#l=factoring(K)
ans=1
l=[]
for n in range(1,K):
    if coprime2(n,K):
        l.append(n)
        ans*=n
        ans=ans%K
if ans%K!=1:
    l.pop()
print(len(l))
for i in range(len(l)):
    l[i]=str(l[i])
print(" ".join(l))
#d={"N":(0,1),"S":(0,-1),"W":(-1,0),"E":(1,0)}

