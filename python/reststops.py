"""
ID: happyn61
LANG: PYTHON3
PROB: reststops
"""

#from collections import defaultdict

import heapq

fin = open ('reststops.in', 'r')
fout = open ('reststops.out', 'w')
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
        
NQ=fin.readline().strip().split()
l=int(NQ[0])
n=int(NQ[1])
ra=int(NQ[2])
rb=int(NQ[3])
ans=0
pre=0
l=[]
stack=[(0,100000000)]
d=[]
mm=0
for i in range(n):
    XY=fin.readline().strip().split()
    x=int(XY[0])
    y=int(XY[1])
    while stack and stack[-1][1]<=y:
        stack.pop()
    stack.append((x,y))
#print(stack)
for i in range(1,len(stack)):
    ans+=(ra-rb)*stack[i][1]*(stack[i][0]-stack[i-1][0])
    
print(ans)

fout.write (str(ans)+'\n')
fout.close()
