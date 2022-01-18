"""
ID: happyn61
LANG: PYTHON3
PROB: hamming
"""

def solveNQ(num,n,c,D,d):
    #print(num,n,c,D,d)
    if c>=len(num):
        print(num)
        rr=""
        rl=[]
        k=0
        for ii in num:
            #rr=""
            
            rr+=" "+str(ii)
            k+=1
            print(k)
            if k==10:
                k=0
                rl.append(rr)
                rr=""
                
            #print(rr)
        if k>0:
            rl.append(rr)
        print(rl)
        for ll in rl:
            fout.write (ll[1:]+"\n")
        return True
    for i in range(n):
        good=True
        for j in range(c):
            if d[num[j]][i] <D:
                good=False
                break
        if good:
            num[c]=i
            if solveNQ(num,n,c+1,D,d):
                #return True
                #print(num)
                return True
    return False        

fin = open ('hamming.in', 'r')
fout = open ('hamming.out', 'w')
#print(dic["4734"])
NBD=fin.readline().strip().split()
N=int(NBD[0])
B=int(NBD[1])
D=int(NBD[2])
#pl=primes(M)
n=2**B
matrix = [[0]*n for i in range(n)]
mat=[0] * n
num=[0] * N
for i in range(n):
    d=0
    j=i
    while j > 0:
        if j%2:
            d+=1
        j=j//2
    mat[i]=d
#print(mat)
#matrixc = [[0]*N for i in range(M)]
#matrixw = [[ [0]*2 for k in range(N) ]for i in range(M)] #E,N
#print(matrixw)
seta=set()
heapset=set()
for i in range(n):
    for j in range(n):
        k=i^j
        
        matrix[i][j]=mat[k]
            

#print(matrix)
#print(seta)
print(n,D)
solveNQ(num,n,0,D,matrix)

        

fout.close()
