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
    AB=sys.stdin.readline().strip().split()
    n=int(AB[0])
    m=int(AB[1])
    #l=sys.stdin.readline().strip().split()
    #s1=sys.stdin.readline().strip()
    #s2=sys.stdin.readline().strip()
    l=sys.stdin.readline().strip()
    pre=[(0,0,0)]
    post=[(0,0,0)]
    a=0
    b=0
    for i in range(n):
        if l[i]=="+":
            a+=1
        else:
            a-=1
        pre.append((min(pre[-1][0],a),max(pre[-1][1],a),a))
    for i in range(n-1,-1,-1):
        if l[i]=="-":
            b+=1
        else:
            b-=1
        post.append((min(post[-1][0],b),max(post[-1][1],b),b))
    for q in range(m):
        AB=sys.stdin.readline().strip().split()
        ll=int(AB[0])-1
        rr=int(AB[1])-1
        m1=min(pre[ll][0],pre[ll][2]+post[n-1-rr][0]-post[n-1-rr][2])
        m2=max(pre[ll][1],pre[ll][2]+post[n-1-rr][1]-post[n-1-rr][2])
        print(m2-m1+1)
        #print(pre,post,ll,rr,m1,m2,pre[ll],post[n-1-rr],post[n-1-rr][2])
    #if F:
    #    print("yes")
    #else:
    #    print("no")
    #return True
    
#for x,y in occupy:
#    l[x][y]="X"
#for ll in l:
#    print("".join(ll))

