"""
ID: happyn61
LANG: PYTHON3
PROB: loan
"""

#from collections import defaultdict
import sys
import heapq

fin = open ('loan.in', 'r')
fout = open ('loan.out', 'w')
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
NQ=fin.readline().strip().split()
#n=int(fin.readline().strip())
N=int(NQ[0])
K=int(NQ[1])
M=int(NQ[2])
hi=N//(N//K+1)
#print(N//M+1,N,hi)
lo=1
def check(n):
    t=N
    for i in range(K):
        #print(n,t,i)
        if t//n>M:
            t-=t//n
            if t<=0:
                return True
        else:
            if (K-i)*M>=t:
                return True
            else:
                return False
    return False

ans=0
#print(N,K,M,hi,lo)
while lo<=hi:
    mi=(lo+hi)//2
    if check(mi):
        ans=mi
        lo=mi+1
    else:
        hi=mi-1
        

print(ans)

fout.write (str(ans)+'\n')
fout.close()
