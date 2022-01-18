"""
ID: happyn61
LANG: PYTHON3
PROB: subset
"""

	    

fin = open ('subset.in', 'r')
fout = open ('subset.out', 'w')
nl=[]
ns=[]
N = int(fin.readline().strip())
k=((N*(N+1))//2)+1
m= [[0 for x in range(k)] for y in range(N+1)] 
m[0][0]=1
for i in range(N):
    ii=i+1
    for j in range(k):
        if j-ii>=0:
            m[ii][j]=m[ii-1][j]+m[ii-1][j-ii]
        else:
            m[ii][j]=m[ii-1][j]
print(N,k)
print((m[N][(k-1)//2])//2)

r=0
if (k-1) % 2 ==0 :
    print("even")
    print(k)
    r= (m[N][(k-1)//2])//2
print(r)
fout.write(str(r)+"\n")
                
fout.close()
    
