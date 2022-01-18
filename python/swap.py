"""
ID: happyn61
LANG: PYTHON3
PROB: swap
"""
FN="swap"
import collections,heapq,time
from itertools import combinations 
import sys
INF=999999
AL="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
al="abcdefghijklmnopqrstuvwxyz"
cost={}
visited=set()
hcost=[]
d={}

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
def fit(n,ol,limit):
    k=0
    i=0
    F=True
    p=-1
    while i<len(ol):
        if F:
            p=ol[i][0]
            F=False
            k+=1
            
        else:
            if p+n<=ol[i][1]:
                #print(ol[i],p,n)
                ps=max(p+n,ol[i][0])
                m=(ol[i][1]-ps)//n+1
                p=ps+m*n-n
                k+=m
                i+=1
            else:
                i+=1
        if k>=limit:
            #print(n)
            return True
    return False
                
ans=0
BIG=1000
print("--- %s seconds ---" % (time.time()))
fin = open (FN+'.in', 'r')
fout = open (FN+'.out', 'w')
N,M,K=fin.readline().strip().split()
#N=fin.readline().strip()
n=int(N)
m=int(M)
k=int(K)
ol=[i for i in range(n)]
def sw(i,j):
    for k in range((j-i+1)//2):
        t=ol[i+k]
        ol[i+k]=ol[j-k]
        ol[j-k]=t
ll=[]
for t in ol:
    ll.append(t)
swl=[]
for i in range(m):
    L,R=fin.readline().strip().split()
    l=int(L)-1
    r=int(R)-1
    swl.append((l,r))
#print(swl)
for t in swl:
    sw(t[0],t[1])
#    print(t,ol)
d={}
for i in range(n):
    d[i]=ol[i]
#print(d)
#mm=[[i for i in range(n)] for j in range(k+1)]
steps=[[] for i in range(n) ]
print("--- %s seconds ---" % (time.time()))
for i in range(n):
    if len(steps[i])>0:
        continue
    s=set()
    lll=[]
    lll.append(i)
    s.add(i)
    c=1
    st=i
    ddindex={}
    ddindex[st]=0
    while d[st] not in s:
        s.add(d[st])
        lll.append(d[st])
        ddindex[d[st]]=len(lll)-1
        st=d[st]
        c+=1
    lsteps=len(steps)
    for t in s:
        #print(ddindex,t)
        kkk=(ddindex[t]+1)%lsteps
        steps[t]=lll[kkk:]+lll[:kkk]
    #print(i,lll,steps)
#print(steps[0])
print("--- %s seconds ---" % (time.time()))
for j in range(n):
    rs=(k-1)%len(steps[j])
    st=j
    #print(j,rs,steps[j][rs])
    mm[-1][j]=steps[j][rs]
#for i in range(k):
#print("--- %s seconds ---" % (time.time() - start_time))
#print(ans)
#print("--- %s seconds ---" % (time.time() - start_time))        
#print(ans)
#print(ans,"asda")
#print(mm[-1])
print("--- %s seconds ---" % (time.time()))
for i in range(n):
    #print(ol[i]+1)
    fout.write(str(mm[-1][i]+1)+"\n")            
fout.close()
