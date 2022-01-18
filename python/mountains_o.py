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

fin = open ('mountains.in', 'r')
fout = open ('mountains.out', 'w')
n=int(fin.readline().strip())
t=0
color=0
colorct=[0]
p=[]


for i in range(n):
    l=list(map(int,fin.readline().strip().split()))
    p.append(l)

p.sort(key=lambda x: x[1],reverse=True)
m=[]
for i in range(n):
    y=p[i][1]
    x=p[i][0]
    cover=False
    for j in range(len(m)):
        if x-y>=m[j][0] and y+x<=m[j][1]:
            cover=True
            break
    if cover==False:
        l=[0,0]
        l[0]=x-y
        l[1]=y+x
        m.append(l)
area=0
#print(m)
fout.write (str(len(m))+'\n')

fout.close()
