"""
ID: happyn61
LANG: PYTHON3
PROB: loan
"""

#from collections import defaultdict
import sys
import heapq

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
#N=int(NQ[0])
#D=int(NQ[1])
for i in range(n):
    d={1:0,2:0}
    a=0
    b=0
    m=int(sys.stdin.readline().strip())
    K=sys.stdin.readline().strip().split()
    l=[]
    for k in K:
        l.append(int(k))
        
    l.sort(reverse=True)
    for i in range(len(l)):
        if i%2==0:
            if l[i]%2==0:
                a+=l[i]
        else:
            if l[i]%2:
                b+=l[i]
    if a==b:
        print("Tie")
    elif a>b:
        print("Alice")
    else:
        print("Bob")
#for x,y in occupy:
#    l[x][y]="X"
#for ll in l:
#    print("".join(ll))

