"""
ID: happyn61
LANG: PYTHON3
PROBLEM NAME: snakes
"""

#def sumdiff(l):
    
fin = open ('snakes2.in', 'r')
fout = open ('snakes.out', 'w')
n=0 
M,N=map(int,fin.readline().strip().split())
print(M)
print(N)

matrix = [[[0]*3 for j in range(M)] for i in range(N+1)]
a=[0]*M
s=[0]*(M+1)
s[0]=0
b=fin.readline().strip().split()
#print(matrix)
for i in range(0,M):
#    x,y=map(int,fin.readline().strip().split())
    a[i]=int(b[i])
    s[i+1]=a[i]+s[i]
        
#    print(x,y)

m=[[0]*M for i in range(M)]

for i in range(M):
    mm=0
    for j in range(i,M):
        if a[j]>mm:
            mm=a[j]
        m[i][j]=mm*(j-i+1)-(s[j+1]-s[i])
print(a,s,m)
        
for i in range(0,N+1):
    for j in range(i,M):
        if i==0:
            if j==0:
                
                matrix[i][j][0]=0
                matrix[i][j][1]=a[j]
            else:
                if a[j]>=matrix[i][j-1][1]:
                    matrix[i][j][0]=(matrix[i][j-1][2]+1)*(a[j]-matrix[i][j-1][1])+matrix[i][j-1][0]
                    matrix[i][j][1]=a[j]
                else:
                    matrix[i][j][0]=(-a[j]+matrix[i][j-1][1])+matrix[i][j-1][0]
                    matrix[i][j][1]=matrix[i][j-1][1]
                    matrix[i][j][2]=matrix[i][j-1][2]+1
        else:
            z=matrix[i-1][i-1][0]+m[i][j]
                
            for k in range(i,j+1):
               x=matrix[i-1][k-1][0]
               if x+m[k][j]<z:
                   z=x+m[k][j]
               #print(i,j,k,x,m[k][j],z)
                
            matrix[i][j][0]=z
            #matrix[i][j][1]=a[j]
                   
            '''if i==j:
                matrix[i][j][0]=0
                matrix[i][j][1]=a[j]
            else:
                x=matrix[i-1][j-1][0]
                if a[j]>matrix[i][j-1][1]:
                    y=(matrix[i][j-1][2]+1)*(a[j]-matrix[i][j-1][1])+matrix[i][j-1][0]
                    #matrix[i][j][1]=a[j]
                else:
                    y=(-a[j]+matrix[i][j-1][1])+matrix[i][j-1][0]
                if x==y:
                    print("really")
                if x<y:
                    matrix[i][j][0]=x
                    matrix[i][j][1]=a[j]
                    print(i,j,"downright")
                else:
                    matrix[i][j][0]=y
                    matrix[i][j][1]=max(a[j],matrix[i][j-1][1])
                    matrix[i][j][2]=matrix[i][j-1][2]+1
                    print(i,j,"down")
              '''      
                
            
#print(a)
#print(matrix)
#print(b)
n=matrix[N][M-1][0]
print(n)
fout.write (str(n) + '\n')
fout.close()
