"""
ID: happyn61
LANG: PYTHON3
PROB: loan
"""

#from collections import defaultdict
import sys
import heapq
from collections import deque

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

#NQ=sys.stdin.readline().strip().split()

n=int(sys.stdin.readline().strip())
#N1=int(NQ[0])
#N2=int(NQ[1])
#N3=int(NQ[1])

for j in range(n):
    #AB=sys.stdin.readline().strip().split()
    #a=int(AB[0])
    #b=int(AB[1])
    #l=sys.stdin.readline().strip().split()
    s1=sys.stdin.readline().strip()
    s2=sys.stdin.readline().strip()
    a=len(s1)
    b=len(s2)
    def gcd(a,b):
        if b%a==0:
            return a
        elif a==1:
            return 1
        else:
            return gcd(b,a-b*(a//b))
    lcm=0
    if a>b:
        lcm=a*b//gcd(b,a)
    else:
        lcm=a*b//gcd(a,b)
    if s1*(lcm//a)==s2*(lcm//b):
        print(s1*(lcm//a))
    else:
        print(-1)
        
    
    #if F:
    #    print("yes")
    #else:
    #    print("no")
    #return True
    
#for x,y in occupy:
#    l[x][y]="X"
#for ll in l:
#    print("".join(ll))

