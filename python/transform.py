"""
ID: happyn61
LANG: PYTHON3
PROB: transform
"""
def fwct(lo,i,step):
    l=lo.copy()
    color=l[i]
    n=i%N
    c=1
    print(l[n])
    n=(n+step)%N
    while (l[n]=='w' or l[n] == color) and l[n]!='d' :
        
        
        c=c+1
        if color =='w' and l[n] != color:
            color=l[n]
        print(n,color)
        l[n]='d'
        n=(n+step)%N
    print(c)
    return c

fin = open ('transform.in', 'r')
fout = open ('transform.out', 'w')
N=int(fin.readline().strip())
m1 = [[0 for x in range(N)] for y in range(N)] 
m2 = [[0 for x in range(N)] for y in range(N)] 
for i in range(N):
    ml=list(fin.readline().strip())
    #print(type(strt),ml,ml[0])
    for j in range(N):
        #print(ml,i,j)
        m1[i][j]=ml[j]

for i in range(N):
    ml=list(fin.readline().strip())
    #print(type(strt),ml,ml[0])
    for j in range(N):
        #print(ml,i,j)
        m2[i][j]=ml[j]
diff=False
maxx=0
if maxx==0:
    maxx=1
    for i in range(N):
        for j in range(N):
            if not diff:
                if m1[i][j] != m2[j][N-1-i]:
                    diff=True
                    maxx=0
    
#print(maxx)
diff=False
if maxx==0:
    maxx=2
    for i in range(N):
        for j in range(N):
            if not diff:
                #print(m1[i][j],m2[N-1-i][N-1-j])
                if m1[i][j] != m2[N-1-i][N-1-j]:
                    #print(m1[i][j],m2[N-1-i][N-1-j])
                    diff=True
                    maxx=0
#print(maxx)
diff=False
if maxx==0:
    maxx=3
    for i in range(N):
        for j in range(N):
            if not diff:
                if m1[i][j] != m2[N-1-j][i]:
                    diff=True
                    maxx=0
diff=False
if maxx==0:
    maxx=4
    for i in range(N):
        for j in range(N):
            if not diff:
                if m1[i][j] != m2[i][N-1-j]:
                    diff=True
                    maxx=0
diff=False
if maxx==0:
    maxx=5
    for i in range(N):
        for j in range(N):
            if not diff:
                if m1[i][j] != m2[N-1-j][N-1-i]:
                    diff=True
                    maxx=0
diff=False
if maxx==0:
    maxx=5
    for i in range(N):
        for j in range(N):
            if not diff:
                if m1[i][j] != m2[N-1-i][j]:
                    diff=True
                    maxx=0
diff=False
if maxx==0:
    maxx=5
    for i in range(N):
        for j in range(N):
            if not diff:
                if m1[i][j] != m2[j][N-1-i]:
                    diff=True
                    maxx=0
diff=False                   
if maxx==0:
    maxx=6
    for i in range(N):
        for j in range(N):
            if not diff:
                if m1[i][j] != m2[i][j]:
                    diff=True
                    maxx=0
diff=False
if maxx==0:
    maxx=7
                    
#print(m1,m2)

current=0
color='w'
start=False
k=0
cw=0
print(maxx)

fout.write (str(maxx)+'\n')
    
#    print(names[i] + ' '+str(money[i])+'\n')
    
fout.close()
