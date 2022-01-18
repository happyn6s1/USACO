"""
ID: happyn61
LANG: PYTHON3
PROB: money
"""
rr=0
fin = open ('money.in', 'r')
fout = open ('money.out', 'w')
cl=[]

def change(n,v,k):
    global rr
    if k==v-1:
        if n%ll[k]==0:
            cl[k]=n//ll[k]
            print(cl)
            rr=rr+1
    else:
        a=0
        while n-a*ll[k]>=0:
           cl[k]=a           
           change(n-a*ll[k],v,k+1)
           #print(n-a*ll[k],k,a)
           a+=1
           
       
VN = fin.readline().strip().split()
V=int(VN[0])
N=int(VN[1])
ll=[]
cc=[[0 for i in range(N+1)] for j in range(V)]
cc[0][0]=1
c=[]
c1=list(map(int,fin.readline().strip().split()))
while c1:
    c=c+c1
    c1=list(map(int,fin.readline().strip().split()))
rr=0
cs=set(c)
print(cs)
c=list(cs)
c.sort()
V=len(c)
for i in range(V):
    ii=i+1
    for j in range(N+1):
        if j==0:
            cc[i][j]=1
        elif i==0:
            if j%c[i]==0:
                cc[i][j]=1
            else:
                cc[i][j]=0
            
        elif j-c[i]>=0:
            cc[i][j]=cc[i][j-c[i]]+cc[i-1][j]
        else:
            cc[i][j]=cc[i-1][j]
            
#print(cc)
rr=cc[V-1][N]
print(rr)
fout.write(str(rr)+"\n")
                
fout.close()
    
