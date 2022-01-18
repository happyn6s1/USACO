"""
ID: happyn61
LANG: PYTHON3
PROB: loan
"""

#from collections import defaultdict
import sys
import heapq
from collections import deque

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]
def factor(n,l,d):
    F=False
    for p in l:
        if n%p==0:
            if p in d:
                d[p]+=1
            else:
                d[p]=1
            F=True
            break
    if F:
        factor(n//p,l,d)
            
#fin = open ('loan.in', 'r')
#fout = open ('loan.out', 'w')
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

#NQ=sys.stdin.readline().strip().split()

n=int(sys.stdin.readline().strip())
#N1=int(NQ[0])
#N2=int(NQ[1])
#N3=int(NQ[1])

for j in range(n):
    AB=sys.stdin.readline().strip().split()
    #a=int(sys.stdin.readline().strip())
    a=int(AB[0])
    b=int(AB[1])
    #k=int(AB[2])
    #al=[0 for i in range(a)]
    #bl=[0 for i in range(b)]
    ak=sys.stdin.readline().strip().split()
    bk=sys.stdin.readline().strip().split()
    h1=[]
    h2=[]
    h3=[]
    h4=[]
    ans=0
    for i in range(a):
        ak[i]=int(ak[i])
        
        bk[i]=int(bk[i])
        if bk[i]==1:
            h1.append(ak[i])
            #h3.append(ak[i])
        else:
            h2.append(ak[i])
            #h4.append(ak[i])
    if (sum(h1)+sum(h2))<b:
        print(-1)
        continue
    h1.sort()
    h2.sort()
    
    bb=b
    while b>0:
        sa=0
        sb=0
        #print(b,ans,h1,h2)
        if len(h1)>=2:
            sa=h1[-1]+h1[-2]
        elif h1:
            sa=h1[-1]
        if h2:
            sb=h2[-1]
        if sb>=sa:
            #print(h1,h2,sa,sb)
            if h2:
                b-=h2.pop()
                ans+=2
        else:
            #print("pop")
            if h1:
                b-=h1.pop()
                ans+=1
            if h1:
                b-=h1.pop()
                ans+=1
    for i in range(a):
        if bk[i]==1:
            h3.append(ak[i])
        else:
            h4.append(ak[i])
    h3.sort()
    h4.sort()
    ans2=0
    b=bb
    if h3:
        ans2+=1
        b-=h3.pop()
        while b>0:
            sa=0
            sb=0
            #print(b,h3,h4,sa,sb)
            if len(h3)>=2:
                sa=h3[-1]+h3[-2]
            elif h3:
                sa=h3[-1]
            if h4:
                sb=h4[-1]
            
            if sb>=sa:
                b-=h4.pop()
                ans2+=2
            else:
                if h3:
                    b-=h3.pop()
                    ans2+=1
                if h3:
                    b-=h3.pop()
                    ans2+=1
        ans=min(ans,ans2)
    print(ans)


#    print("".join(l))
    #print(s)
    #l=sys.stdin.readline().strip().split()
    #s1=sys.stdin.readline().strip()
    #s2=sys.stdin.readline().strip()
    
        #print(pre,post,ll,rr,m1,m2,pre[ll],post[n-1-rr],post[n-1-rr][2])
    #if F:
    #    print("yes")
    #else:
    #    print("no")
    #return True
    
#for x,y in occupy:
#    l[x][y]="X"
#for ll in l:
#    print("".join(ll))

