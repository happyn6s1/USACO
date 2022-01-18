"""
ID: happyn61
LANG: PYTHON3
PROB: measurement
"""
import heapq
fin = open ('measurement.in', 'r')
fout = open ('measurement.out', 'w')
N,G=list(map(int,fin.readline().strip().split()))
ll=[]
d={} #index to amount
dd={} #amount to set
k=0
ds={}
ans=0
#from datetime import datetime
#print(datetime.now())
for i in range(N):
    a,b,c=list(map(int,fin.readline().strip().split()))
    ll.append((a,b,c))
    #print(a,b,c)
ll.sort()
m=0
h=[]
oldset=set()
for a,b,c in ll:
    if b not in d:
        d[b]=c
        if d[b] in dd:
            dd[d[b]].add(b)
        else:
            dd[d[b]]=set()
            dd[d[b]].add(b)
        heapq.heappush(h,-d[b])    
        
    else:
        #print(d,dd,b)
        dd[d[b]].remove(b)
        d[b]+=c
        if d[b] in dd:
            dd[d[b]].add(b)
        else:
            dd[d[b]]=set()
            dd[d[b]].add(b)
        heapq.heappush(h,-d[b])
    while heapq.nsmallest(1,h)==set():
        heapq.heappop(h)
    #print("==",b,c,d,dd,h)
    if len(h)==0:
        if oldset!=set():
            ans+=1
            oldset=set()
    else:
        
        if oldset!=dd[-h[0]]:
            ans+=1
            #print(ans,oldset,dd[-h[0]])
            oldset=dd[-h[0]].copy()
#print(datetime.now())
print(ans)
fout.write(str(ans)+"\n")
                
fout.close()
    
