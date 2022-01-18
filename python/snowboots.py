"""
ID: happyn61
LANG: PYTHON3
PROB: snowboots
"""

#from collections import defaultdict

import heapq

fin = open ('snowboots.in', 'r')
fout = open ('snowboots.out', 'w')
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
n=int(NQ[0])
b=int(NQ[1])
ans=0
pre=0
l=[]
bt=[]
MAX=99999
dp=[MAX for i in range(n)]
dp[0]=-1
mm=0
XY=fin.readline().strip().split()

for i in range(n):
    l.append(int(XY[i]))
for i in range(b):
    XY=fin.readline().strip().split()
    bt.append((int(XY[0]),int(XY[1])))
#print(stack)
for i in range(1,n):
    for k in range(b):
        #print(i,j,bt,i-bt[j][1],l[i-bt[j][1]],l[i])
        for j in range(1,1+bt[k][1]):
            #print(i,k,j)
            if i-j>=0 and l[i]<=bt[k][0] and l[i-j]<=bt[k][0] and k>=dp[i-j]:
                dp[i]=min(k,dp[i])
print(dp)
ans=dp[-1]    
print(ans)

fout.write (str(ans)+'\n')
fout.close()
