"""
ID: happyn61
LANG: PYTHON3
PROB: ttwo
"""
FN="ttwo"
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
#N=int(fin.readline().strip())
#MN=fin.readline().strip().split()
#M=int(MN[0])
#N=int(MN[1])
    #print(ans)
ans=0
f=[]
c=[]
fd=0
cd=0
dt=[(-1,0),(0,1),(1,0),(0,-1)]
m=[[0 for j in range(10)] for i in range(10)]
for i in range(10):
    ss=fin.readline().strip()
    for j in range(10):
        print(ss[j])
        if ss[j]=="F":
            f=[i,j]
        elif ss[j]=="C":
            c=[i,j]
        elif ss[j]=='*':
            #print("catch")
            m[i][j]=1
#print(m)
s=set()

while f!=c:
    #print(ans,f,c,fd,cd)
    if (f[0],f[1],fd,c[0],c[1],cd) in s:
        ans=0
        break
    s.add((f[0],f[1],fd,c[0],c[1],cd))
    ans+=1
    ti=f[0]+dt[fd][0]
    tj=f[1]+dt[fd][1]
    #print(ti,tj,m[ti][ti])
    if ti>=0 and ti<=9 and tj>=0 and tj<=9 and m[ti][tj]==0:
        f=[ti,tj]
    else:
        fd=(fd+1)%4
    ti=c[0]+dt[cd][0]
    tj=c[1]+dt[cd][1]
    if ti>=0 and ti<=9 and tj>=0 and tj<=9 and m[ti][tj]==0:
        c=[ti,tj]
    else:
        cd=(cd+1)%4
    
print(ans)
fout.write(str(ans)+"\n")            
fout.close()
