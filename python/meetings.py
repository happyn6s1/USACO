"""
ID: happyn61
LANG: PYTHON3
PROB: moobuzz
"""

#from collections import defaultdict

import heapq

fin = open ('meetings.in', 'r')
fout = open ('meetings.out', 'w')
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
L=int(NQ[1])
l=[]
ol=[]
totalw=0
for i in range(n):
    wxd=fin.readline().strip().split()
    w=int(wxd[0])
    x=int(wxd[1])
    d=int(wxd[2])
    ol.append((x,d,w))
    totalw+=w
    if d==1:
        l.append((L-x,d))
    else:
        l.append((x,d))
l.sort(reverse=True)
ol.sort()
ww=0
i=0
j=0
k=0
p=0
while ww*2<totalw:
    p=l.pop()
    
    if p[1]==-1:
        ww+=ol[i][2]
        i+=1
    else:
        ww+=ol[j][2]
        j-=1
    #print(p,totalw,ww)
    #print(ww,totalw,j)
t=p[0]
ans=0
for i in range(n):
    for j in range(n):
        #print(ol[i],ol[j])
        if ol[i][0]<ol[j][0] and ol[j][0]-ol[i][0]<=t*2 and ol[i][1]==1 and  ol[j][1]==-1:
            ans+=1
print(t,ans)
fout.write (str(ans)+'\n')
fout.close()
