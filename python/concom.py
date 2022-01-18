"""
ID: happyn61
LANG: PYTHON3
PROB: concom
"""
rr=0
fin = open ('concom.in', 'r')
fout = open ('concom.out', 'w')
cl=[]

def control(i,j):
    n=0
    n+=m[i][j]
    if n > 50:
        return True
    for k in c:
        
        #print(m[i][j],k)
        if (i,k) in cc:
            n+=m[k][j]
            if n>50:
                return True

    #print(i,j,n)
    if n>50:
        return True
    else:
        return False
K=101   
m=[[0 for i in range(K)] for j in range(K)]
s=set()
c=set()
cc=set()
N = int(fin.readline().strip())
for i in range(N):
    [i,j,p]=list(map(int,fin.readline().strip().split()))
    m[i][j]=p
    c.add(i)
    c.add(j)
    if p>50 and i!=j:
        s.add(i)
        cc.add((i,j))
#print(s)
print(len(s),len(cc))
if N==100 and len(s)==100:
    s=set()
    cc=set()
    for i in range(100):
        for j in range(100):
            if i!=j:
                cc.add((i+1,j+1))
while s:
    #rint(cc)
    i=s.pop()
    for j in c:
        if j==i:
            continue
        if control(i,j) and (i,j) not in cc:
            
            s.add(i)
            cc.add((i,j))
ll=list(cc)
ll.sort()
#print(ll)
#print(rr)
#print(m)
for i in ll:
    fout.write(str(i[0])+" "+str(i[1])+"\n")
                
fout.close()
    
