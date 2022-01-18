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
K=sys.stdin.readline().strip().split()
H=int(K[0])
W=int(K[1])
m=[]
for i in range(H):
    l=sys.stdin.readline().strip()
    m.append(l)
        
x=0 #c
y=0 #r
while True:
    if m[y][x]=="*":
        
        ans+=1
    
    if (x==W-1 and y==H-1):
        break
    elif x==W-1:
        y+=1
    elif y==H-1:
        x+=1
    else:
        F=True
        for i in range(1,5):
            #print(m,x,y,i,ans)

            if x+i<W and m[y][x+i]=="*":
                break
            elif y+i<H and m[y+i][x]=="*":
                F=False
                break
        #print(x,y,F)
        if F:
            x+=1
        else:
            y+=1
print(ans)
