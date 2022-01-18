"""
ID: happyn61
LANG: PYTHON3
PROB: poetry
"""

fin = open ('poetry.in', 'r')
fout = open ('poetry.out', 'w')
N,M,K=list(map(int,fin.readline().strip().split()))
ll=[]
d={}
k=0
ds={}
from datetime import datetime
print(datetime.now())
for i in range(N):
    a,b=list(map(int,fin.readline().strip().split()))
    
    if b not in d:
        
        d[b]=k
        #ll.append({})
        dd={}
        dd[a]=1
        ll.append(dd)
        k+=1
    else:
        #print(ll,d,a,b,ll[d[b]])
        if a in ll[d[b]]:
            ll[d[b]][a]+=1
        else:
            dd=ll[d[b]]
            #print(dd)
            dd[a]=1
    if a in ds:
        ds[a]+=1
    else:
        ds[a]=1
        
dm={}
x=0
for i in range(M):
    a=fin.readline().strip()
    if a not in dm:
        dm[a]=1
    else:
        dm[a]+=1
    x=max(x,dm[a])
l=[1 for i in range(K+1)]
l[0]=1
print(datetime.now())
#print(ds,dm)
for i in range(1,K+1):
    ss=0
    for j in ds:
        if i-j>=0:
            
            ss+=l[i-j]*(ds[j])
    l[i]=ss
#print(l)
print(datetime.now(),"before dp")
cl=[0 for i in range(len(d))]
for k in d:
    ss=0
    #print(ll[d[k]])
    for kk in ll[d[k]]:
        if kk<=K:
            ss+=l[K-kk]*ll[d[k]][kk]
            ss=ss%(10**9+7)
    cl[d[k]]=ss
print(len(cl))
r=[1 for j in range(x+1)]
rr=[[1 for i in range(len(cl))] for j in range(x+1)]
print(datetime.now(),x)
for i in range(1,x+1):
    for j in range(len(cl)):
        rr[i][j]=rr[i-1][j]*cl[j]
    r[i]=sum(rr[i])%(10**9-7)
ans=1
print("slow",datetime.now())
for k in dm:
    ans*=r[dm[k]]
    ans=ans%(10**9+7)
print(ans%(10**9+7))
print(datetime.now())
fout.write(str(ans%(10**9+7))+"\n")
                
fout.close()
    
