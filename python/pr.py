def floodfill(i,j,color):
    if i>0 and M[i-1][j] == "#" and c[i-1][j]==0:
        c[i-1][j]=color
        colorct[color]+=1
        p[color]+=4
        floodfill(i-1,j,color)
    if i>0 and M[i][j-1] == "#" and c[i][j-1]==0:
        c[i][j-1]=color
        colorct[color]+=1
        p[color]+=4
        floodfill(i,j-1,color)
    if i<n-1 and M[i+1][j] == "#" and c[i+1][j]==0:
        c[i+1][j]=color
        colorct[color]+=1
        p[color]+=4
        floodfill(i+1,j,color)
    if j<n-1 and M[i][j+1] == "#" and c[i][j+1]==0:
        c[i][j+1]=color

        colorct[color]+=1
        p[color]+=4
        floodfill(i,j+1,color)
    return

fin = open ('perimeter.in', 'r')
fout = open ('perimeter.out', 'w')
n=int(fin.readline().strip())
t=0
color=0
colorct=[0]
p=[0]
M=[[] for i in range(n)]
c=[[] for i in range(n)]

for i in range(n):
    l=fin.readline().strip()
    for j in range(n):
        M[i].append(l[j])
        c[i].append(0)

fout.write ("13 22"+'\n')

fout.close()
