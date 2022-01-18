"""
ID: happyn61
LANG: PYTHON3
PROB: comehome
"""
FN="comehome"
import collections,heapq
import sys
AL="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
al="abcdefghijklmnopqrstuvwxyz"
cost={}
visited=set()
hcost=[]
d={}
INF=999999
for i in AL:
    d[i]=[]
    cost[i]=-1
    heapq.heappush(hcost,(INF,i))
for i in al:
    d[i]=[]
    cost[i]=-1
    heapq.heappush(hcost,(INF,i))
heapq.heappush(hcost,(0,"Z"))
cost['Z']=0
fin = open (FN+'.in', 'r')
fout = open (FN+'.out', 'w')
N=int(fin.readline().strip())
for i in range(N):
    A,B,W=fin.readline().strip().split()
    w=int(W)
    heapq.heappush(d[A],(w,B))
    heapq.heappush(d[B],(w,A))
#print(d,hcost)
r1=""
r2=0
#fout.write (a[-r:] + '\n')
while hcost:
    v=heapq.heappop(hcost)
    if v[1] in visited:
        continue
    visited.add(v[1])
    ww=v[0]
    for i in d[v[1]]:
        heapq.heappush(hcost,(i[0]+ww,i[1]))
    if v[1]>="A" and v[1]<"Z":
        r1=v[1]
        r2=v[0]
        break
print(r1,r2)
fout.write(r1+" "+str(r2)+"\n")
fout.close()
