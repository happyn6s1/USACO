"""
ID: happyn61
LANG: PYTHON3
PROB: maze1
"""
FN="maze1"
import collections,heapq
import sys
INF=999999
AL="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
al="abcdefghijklmnopqrstuvwxyz"
cost={}
visited=set()
hcost=[]
d={}


fin = open (FN+'.in', 'r')
fout = open (FN+'.out', 'w')
#N=int(fin.readline().strip())
MN=fin.readline().strip().split()
M=int(MN[0])
N=int(MN[1])
a=[]
m=[[" " for j in range(2*M+1)] for i in range(2*N+1)]
for i in range(N*2+1):
    stt=fin.readline()
    #print(stt)
    for j in range(2*M+1):
        if j<len(stt) and type(m[i][j])==str:
            m[i][j]=stt[j]
        if m[i][j]==" " and (i==0 or j ==0 or j==2*M or i==2*N):
            #print(i,j)
            if i==0:
                a.append((i+1,j))
                m[i+1][j]=0
                m[i][j]="+"
                
            if j==0:
                print(i,j)
                m[i][j]="+"
                m[i][j+1]=0
                a.append((i,j+1))
                print(m)
            if i==2*N:
                m[i][j]="+"
                a.append((i-1,j))
                m[i-1][j]=0
            if j==2*M:
                m[i][j]="+"
                a.append((i,j-1))
                m[i][j-1]=0
        #print(i,j,m[1][1],type (m[1][1]))
        if type (m[i][j]) != int and m[i][j]==" " and i%2 and j%2:
            m[i][j]=INF
        #print(i,j,m)
#print(d,hcost)
#print(m,a)
#fout.write(r1+" "+str(r2)+"\n")
dq=collections.deque([])
dq.append(a[0])
dq.append(a[1])
while dq:
    (i,j)=dq.popleft()
    #print(i,j,type(m[i][j-1])==int)
    if i>1 and type(m[i-2][j])==int and m[i-2][j]-m[i][j]>1 and m[i-1][j]==" ":
        m[i-2][j]=m[i][j]+1
        dq.append((i-2,j))
    if j>1 and type(m[i][j-2])==int and m[i][j-2]-m[i][j]>1 and m[i][j-1]==" ":
        m[i][j-2]=m[i][j]+1
        dq.append((i,j-2))
        #print("qw")
    if i<2*N-1 and type(m[i+2][j])==int and m[i+2][j]-m[i][j]>1 and m[i+1][j]==" ":

        m[i+2][j]=m[i][j]+1
        dq.append((i+2,j))
    if j<2*M-1 and type(m[i][j+2])==int and m[i][j+2]-m[i][j]>1 and m[i][j+1]==" ":
        m[i][j+2]=m[i][j]+1
        dq.append((i,j+2))
#print(m)
ans=0
for i in range(N*2+1):
    for j in range(2*M+1):
        if type(m[i][j])==int and m[i][j]<INF:
            ans=max(ans,m[i][j])
print(ans)
fout.write(str(ans+1)+"\n")            
fout.close()
