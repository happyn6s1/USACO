"""
ID: happyn61
LANG: PYTHON3
PROB: cowsignal
"""

fin = open ('cowsignal.in', 'r')
fout = open ('cowsignal.out', 'w')
M,N,K=list(map(int,fin.readline().strip().split()))
ll=[]
for i in range(M):
    ll.append(fin.readline().strip())  
l=[["" for j in range(N*K)] for i in range(M*K)]

for i in range(M*K):
    for j in range(N*K):
        l[i][j]=ll[i//K][j//K]
rr=0

for i in range(M*K):        
    fout.write("".join(l[i])+"\n")
                
fout.close()
    
