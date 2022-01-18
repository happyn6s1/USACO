"""
ID: happyn61
LANG: PYTHON3
PROB: mountains
"""
FN="mountains"
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
#N,M,K=fin.readline().strip().split()
N=fin.readline().strip()
n=int(N)
#m=int(M)
#k=int(K)
#ol=[i for i in range(n)]
def sw(i,j):
    for k in range((j-i+1)//2):
        t=ol[i+k]
        ol[i+k]=ol[j-k]
        ol[j-k]=t
ll=[]
l=[]
#ans=n
for i in range(n):
    X,Y=fin.readline().strip().split()
    ll.append((int(X)-int(Y),1,i))
    ll.append((int(X)+int(Y),0,i))
    l.append((int(X)-int(Y),int(X)+int(Y)))
ct=0
ll.sort()
dq=deque([])
s=set()
for a,b,c in ll:
    if b==1:
        dq.append((a,c))
    else:
        while dq and dp[0][1] in s:
            dq.popleft()
        if dq[0][0]==l[c][0]:
            dp.popleft()
        else:
            n+=1
        
print(ll)
print(ans)
#for i in range(k):
#print("--- %s seconds ---" % (time.time() - start_time))
#print(ans)
#print("--- %s seconds ---" % (time.time() - start_time))        
#print(ans)
#print(ans,"asda")
#print(mm[-1])
print("--- %s seconds ---" % (time.time()))
#for i in range(n):
    #print(ol[i]+1)
#    fout.write(str(mm[-1][i]+1)+"\n")            
fout.write(str(ans)+"\n")            
fout.close()
