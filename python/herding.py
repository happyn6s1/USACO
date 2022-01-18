"""
ID: happyn61
LANG: PYTHON3
PROB: herding
"""
FN="herding"
import collections,heapq
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


fin = open (FN+'.in', 'r')
fout = open (FN+'.out', 'w')
N=int(fin.readline().strip())
#MN=fin.readline().strip().split()
#M=int(MN[0])
#N=int(MN[1])
    #print(ans)
ol=[]
ct=0
for i in range(N):
    ol.append(int(fin.readline().strip()))
ol.sort()
target=ol[-1]-ol[0]+1-N
l=[]

for i in range(1,N):
    l.append(ol[i]-ol[i-1])
    if l[-1]!=1:
        #print(l)
        ct+=1
ans=0
#print(l,target)
lo=0
hi=0
m1=INF
m2=0
a=0
s=0
j=0
presum=[0]

for t in l:
    presum.append(presum[-1]+t)
f=False
i=0
while presum[j]-presum[i]<target:
    j+=1

m1=j
m2=j
ii=0
for i in range(j-1,-1,-1):
    #print(j,i,presum)
    while presum[i]+presum[-1]-presum[N-1-ii]<target:
        ii+=1
    #print(i,ii,target)
    m1=min(m1,i+ii)
    m2=max(m2,i+ii)
m2=target-min(l[0],l[-1])+1
if ct==1:
    if target>1:
        m1=2
print(m1,m2)
#print(ans)
fout.write(str(m1)+"\n")            
fout.write(str(m2)+"\n")            
fout.close()
