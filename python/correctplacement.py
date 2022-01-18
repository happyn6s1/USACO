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
    d={}
    a=0
    b=0
    m=int(sys.stdin.readline().strip())
    l=[]
    ans=[-1 for i in range(m)]
    for j in range(m):
        #ans=[]
        
        K=sys.stdin.readline().strip().split()
        a=int(K[0])
        b=int(K[1])
        if a>b:
            t=a
            a=b
            b=t
        if a in d:
            d[a].append((b,j))
        else:
            d[a]=[(b,j)]
            
            l.append((a))
            
    l.sort()
    mh=[99999999999,-1]
    for i in l:
        mm=mh[0]
        kk=-1
        #print(l,d[i],mh,i,d)
        for b,index in d[i]:
            if b>mh[0]:
                #print(i,mh)
                ans[index]=mh[1]+1
            if b<mm:
                 mm=b
                 kk=index
        if kk>=0:
            mh=[mm,kk]
    aa=[]
    for i in range(m):
        aa.append(str(ans[i]))
    print(" ".join(aa))
        
#for x,y in occupy:
#    l[x][y]="X"
#for ll in l:
#    print("".join(ll))

