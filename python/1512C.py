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
#NK=sys.stdin.readline().strip().split()
K=int(sys.stdin.readline().strip())
#N=int(NK[0])
#K=int(NK[1])
#M=int(NK[2])
#ol=list(map(int,sys.stdin.readline().strip().split()))
#d={0:0,1:0}

x=0
y=0

#d={"N":(0,1),"S":(0,-1),"W":(-1,0),"E":(1,0)}
for testj in range(K):
    ans=0
    F=True
    a,b=list(map(int,sys.stdin.readline().strip().split()))
    st=list(sys.stdin.readline().strip())
    if (a+b)!=len(st):
        print(-1)
        continue
    if len(st)%2==1:
        if st[(len(st)-1)//2]=="0":
            a-=1
        elif st[(len(st)-1)//2]=="1":
            b-=1
    for i in range(len(st)//2):
        p=st[i]
        q=st[len(st)-1-i]
        if p=="0" and q=="1" or p=="1" and q=="0":
            F=False
            break
        elif p=="0" and q=="?" or p=="?" and q=="0" or p=="0" and q=="0":
            a-=2
            st[i]="0"
            st[len(st)-1-i]="0"
        elif p=="1" and q=="?" or p=="?" and q=="1" or p=="1" and q=="1":
            b-=2
            st[i]="1"
            st[len(st)-1-i]="1"
        if a<0 or b<0:
            F=False
            break
    if not F:
        print(-1)
    else:
        #print(st,a,b)
        for i in range(len(st)//2):
            p=st[i]
            q=st[len(st)-1-i]
            if p!="?" or q!="?":
                continue
            if a>1:
                st[i]="0"
                st[len(st)-1-i]="0"
                a-=2
            elif b>1:
                st[i]="1"
                st[len(st)-1-i]="1"
                b-=2
        
        if a==1:
            st[(len(st)-1)//2]="0"
            a-=1
            
        elif b==1:
            st[(len(st)-1)//2]="1"
            b-=1
            #print(a,b,st)
        if a==0 and b==0:
            print("".join(st))
        else:
            print(-1)
