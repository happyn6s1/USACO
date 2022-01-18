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
NQ=sys.stdin.readline().strip().split()
#n=int(fin.readline().strip())
N=int(NQ[0])
D=int(NQ[1])
l=[]
occupy=set()

start=[]
for i in range(N):
    ts=sys.stdin.readline().strip()
    tl=[]
    #print(ts)
    for j in range(len(ts)):
        c=ts[j]
        if c=="S":
            start.append((i,j))
        tl.append(c)
    l.append(tl)
#print(l)    
#print(ans,start)
#occupy.add()
stack=[]
s=set()
for st in start:
    stack.append((st[0],st[1],1,0))
    s.add((st[0],st[1],1))
try:
    from functools import lru_cache
except ImportError:
    from backports.functools_lru_cache import lru_cache   
@lru_cache(None)
def check(x,y,size):
    #print("checking",x,y,size)
    F=True
    for i in range(size):
        j=size-1-i
        if l[x+i][y+j]=="#" or l[x-i][y+j]=="#" or l[x+i][y-j]=="#" or l[x-i][y-j]=="#":
            F=False
            break
    return F
while stack:
    x,y,size,step=stack.pop()
    #print(x,y,size,step)
    F=True
    if l[x][y]=="#":
        continue
    if not check(x,y,size):
        continue
    
    for i in range(size):
        j=size-1-i
        #print(st,di,i,j,x,y,step)
        occupy.add((x+i,y+j))
        occupy.add((x-i,y+j))
        occupy.add((x+i,y-j))
        occupy.add((x-i,y-j))

    
    if step%D==0 and step>0:
        size+=1
        if not check(x,y,size):
            F=False
            continue
        for i in range(size):
            if (x,y,size) not in s and check(x,y,size):
                stack.append((x,y,size,step+1))
                s.add((x,y,size))
            #print(st,di,occupy)
    if not F:
        continue
    for di in ((1,0),(0,1),(-1,0),(0,-1)):
        
        if (x+di[0],y+di[1],size) not in s and check(x,y,size):
            #print(s)
            stack.append((x+di[0],y+di[1],size,step+1))
            s.add((x+di[0],y+di[1],size))
#for x,y in occupy:
#    l[x][y]="X"
#for ll in l:
#    print("".join(ll))
print(len(occupy))
