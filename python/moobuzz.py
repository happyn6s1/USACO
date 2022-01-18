"""
ID: happyn61
LANG: PYTHON3
PROB: moobuzz
"""

#from collections import defaultdict

import heapq

fin = open ('moobuzz.in', 'r')
fout = open ('moobuzz.out', 'w')
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

l=[1,2,4,7,8,11,13,14]
n=n-1
a=n//8
b=n%8
ans=15*a+l[b]
print(n,ans)
fout.write (str(ans)+'\n')
fout.close()
