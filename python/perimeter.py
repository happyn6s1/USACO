
n=0
def floodfill2(x, y, Color, n):

    # assume surface is a 2D image and surface[x][y] is the color at x, y.

    theStack = [ (x, y) ]

    while len(theStack) > 0:

        x, y = theStack.pop()

        if x < n-1 and M[x+1][y] == "#" and c[x+1][y]==0:
            c[x+1][y]=color
            colorct[color]+=1
            p[color]+=4
            theStack.append( (x + 1, y) )  # right
        if x > 0 and M[x-1][y] == "#" and c[x-1][y]==0:
            c[x-1][y]=color
            colorct[color]+=1
            p[color]+=4
            theStack.append( (x - 1, y) )  # left
        if y < n-1 and M[x][y+1] == "#" and c[x][y+1]==0:
            c[x][y+1]=color
            colorct[color]+=1
            p[color]+=4
            theStack.append( (x, y + 1) )  # down
        if y> 0 and M[x][y-1] == "#" and c[x][y-1]==0:
            c[x][y-1]=color
            colorct[color]+=1
            p[color]+=4
            theStack.append( (x, y - 1) )  # up

        
def floodfill(i,j,color,n):
    if i>0 and M[i-1][j] == "#" and c[i-1][j]==0 :
        c[i-1][j]=color
        colorct[color]+=1
        p[color]+=4
        floodfill(i-1,j,color,n)
    if j>0 and M[i][j-1] == "#" and c[i][j-1]==0:
        c[i][j-1]=color
        colorct[color]+=1
        p[color]+=4
        floodfill(i,j-1,color,n)
    if j< (n-1) and M[i][j+1] == "#" and c[i][j+1]==0:
        c[i][j+1]=color
        colorct[color]+=1
        p[color]+=4
        floodfill(i,j+1,color,n)
    if i< (n-1) and M[i+1][j] == "#" and c[i+1][j]==0:
        c[i+1][j]=color
        colorct[color]+=1
        p[color]+=4
        floodfill(i+1,j,color,n)
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

for i in range(n):
    for j in range(n):
        if c[i][j]>0 or M[i][j] !="#":
            continue
        color+=1
        colorct.append(1)
        p.append(4)
        c[i][j]=color
        floodfill2(i,j,color,n)

for i in range(n):
    for j in range(n):
        if c[i][j] == 0:
            continue
        if i>0 and M[i-1][j] == "#":
            p[c[i][j]]-=1
        if j>0 and M[i][j-1] == "#":
            p[c[i][j]]-=1
        if i<n-1 and M[i+1][j] == "#" :
            p[c[i][j]]-=1
        if j<n-1 and M[i][j+1] == "#" :
            p[c[i][j]]-=1
        
area=max(colorct)
minp=99999
for i in range(len(p)):
    if colorct[i]<area:
        continue
    if p[i]<minp:
        minp=p[i]
#print(area,minp)
#print(c)
fout.write (str(area)+" "+str(minp)+'\n')
#fout.write ("13 22"+'\n')

fout.close()
