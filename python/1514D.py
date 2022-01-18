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
import random
from math import gcd as bltin_gcd
def coprime2(a, b):
    return bltin_gcd(a, b) == 1
def majorityElement(nums):
        
        majority_count = len(nums)//2
        k=0
        while True:
            if k>10:
                return -1
            k+=1
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate
def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    left_m = get_majority_element(a, left, (left + right - 1)//2 + 1)
    right_m = get_majority_element(a, (left + right - 1)//2 + 1, right)
    left_count = 0
    for i in range(left, right):
        if a[i] == left_m:
            left_count += 1
    if left_count > (right-left)//2:
        return left_m

    right_count = 0
    for i in range(left, right):
        if a[i] == right_m:
            right_count += 1
    if right_count > (right-left)//2:
        return right_m

    return -1
n,Q=list(map(int,sys.stdin.readline().strip().split()))
l=list(map(int,sys.stdin.readline().strip().split()))
d={}
for i in range(n):
    if l[i] in d:
        d[l[i]].append(i)
    else:
        d[l[i]]=[i]
for j in range(Q):
    lf,r=list(map(int,sys.stdin.readline().strip().split()))
    
    #k=get_majority_element(l,lf-1,r)
    k=majorityElement(l[lf-1:r])
    if k<0:
        print(1)
        continue
    #print(k)
    #print(d)

    
    hi=len(d[k])-1
    lo=0
    ll=hi
    while lo<=hi:
        mi=(lo+hi)//2
        if d[k][mi]>=lf-1:
            ll=mi
            hi=mi-1
        else:
            lo=mi+1
    rr=0
    lo=0
    hi=len(d[k])-1
    while lo<=hi:
        mi=(lo+hi)//2
        if d[k][mi]<=r-1:
            rr=mi
            lo=mi+1
        else:
            hi=mi-1
    #print(d,ll,rr,lf,r)
    kk=rr+1-ll
    #print(kk)
    print(r+1-lf-(r+1-lf-kk)*2)
