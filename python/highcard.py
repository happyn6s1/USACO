"""
ID: happyn61
LANG: PYTHON3
PROB: highcard
"""

#from collections import defaultdict

import heapq

fin = open ('highcard.in', 'r')
fout = open ('highcard.out', 'w')
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
        
#NQ=fin.readline().strip().split()
n=int(fin.readline().strip())
ans=0
a=[]
s=set()
b=[]
for i in range(n):
    a.append(int(fin.readline().strip()))
    s.add(a[-1])
a.sort()
for i in range(2*n):
    if i+1 not in s:
        b.append(i+1)
i=0
j=0
while i < n:
    while j<n and b[j]<a[i]:
        j+=1
    #print(i,j)
    if j==n:
        break
    #print(i,j,a,b)
    ans+=1
    i+=1
    j+=1
print(ans)

fout.write (str(ans)+'\n')
fout.close()
