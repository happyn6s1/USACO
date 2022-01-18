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
#N=int(NQ[0])
#D=int(NQ[1])
for j in range(n):
    
    a=0
    b=1
    m=int(sys.stdin.readline().strip())
    d=[[0,0] for i in range(m)]
    
    L=sys.stdin.readline().strip().split()
    if m<3:
        print(0)
        continue
    for i in range(m):
        L[i]=int(L[i])
        
    for i in range(1,m-1):
        x=0
        y=0
        if L[i]>L[i-1]:
            x=1
        elif L[i]<L[i-1]:
            x=-1
        if L[i]>L[i+1]:
            y=-1
        elif L[i]<L[i+1]:
            y=1
        if [x,y]==[-1,1] or [x,y]==[1,-1]:
            a+=1
        d[i]=[x,y]
    #print(d)
    for i in range(1,m-1):
        
        if d[i][0]*d[i][1]==-1:
            k=0
            #print(j,i,k)
            if d[i-1][0]*d[i-1][1]==-1 and d[i+1][0]*d[i+1][1]==-1 :
                k=3
                
            elif d[i-1][0]*d[i-1][1]==-1 or d[i+1][0]*d[i+1][1]==-1 :
                x=0
                y=0
                if L[i-1]>L[i+1]:
                    x=-1
                elif L[i-1]<L[i+1]:
                    x=1
                else:
                    x=0
                
                if x*d[i-1][0]<0:
                    y+=1
                if x*d[i+1][1]<0:
                    y+=1
                #print(x,d[i+1],d[i-1],y)
                if y==2:
                    k=1
                else:
                    k=2
            else:
                x=0
                y=0
                if L[i-1]>L[i+1]:
                    x=-1
                elif L[i-1]<L[i+1]:
                    x=1
                else:
                    x=0
                
                if x*d[i-1][0]<0:
                    y+=1
                if x*d[i+1][1]<0:
                    y+=1
                #print(x,d[i+1],d[i-1],y)
                if y==1:
                    k=0
                else:
                    k=1
            #print(d,i,k)
            b=max(b,k)
    #print(i,a,b)
    print(max(0,a-b))
#for x,y in occupy:
#    l[x][y]="X"
#for ll in l:
#    print("".join(ll))

