"""
ID: happyn61
LANG: PYTHON3
PROB: loan
"""
from datetime import date
from time import gmtime, strftime
from itertools import product
#from collections import defaultdict
import sys
import heapq
from collections import deque
MOD=1000000007
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


n=int(sys.stdin.readline().strip())
graph=[[]for i in range(n)]
el=[]
nl=[]
for i in range(n):
    AB=sys.stdin.readline().strip().split()
    x=int(AB[1])
    y=int(AB[2])
    if AB[0]=="E":
        el.append((x,y,i))
    else:
        nl.append((x,y,i))
steps=[]

nn=n
for e in el:
    for n in nl:
        #cross.append((e[1],n[0])
        if e[1]>=n[1] and n[0]>=e[0]:
            steps.append(e[1]-n[1])
            steps.append(n[0]-e[0])
print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
steps=list(set(steps))
steps.sort()
m={}


#print(el,nl,steps)
parent=[i for i in range(nn)]
alive=[True for i in range(nn)]
print(nn,len(steps))
print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

for i in steps:
    for e in el:
        if not alive[e[2]]:
            continue
       
        if (e[0]+i,e[1]) in m and m[(e[0]+i,e[1])][0]<i:
            #print(e,m)
            parent[e[2]]=m[(e[0]+i,e[1])][1]
            alive[e[2]]=False
        else:
            m[(e[0]+i,e[1])]=[i,e[2]]
    for n in nl:
        if not alive[n[2]]:
            continue
        if (n[0],n[1]+i) in m and m[(n[0],n[1]+i)][0]<i:
            parent[n[2]]=m[(n[0],n[1]+i)][1]
            alive[n[2]]=False
        else:
            m[(n[0],n[1]+i)]=[i,n[2]]
    #print(parent,m)
print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
#print(parent)
tree=[[] for i in range(nn)]
ans=[-1 for i in range(nn)]
for i in range(nn):
    if parent[i]!=i:
        tree[parent[i]].append(i)
print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
#print(tree)
def nc(n):
    ret=len(tree[n])
    for c in tree[n]:
        ret+=nc(c)
    ans[n]=ret
    return ret
for i in range(nn):
    if ans[i]<0:
        nc(i)

#print(ans)
for n in ans:
    print(n)
#print(len(occupy))
