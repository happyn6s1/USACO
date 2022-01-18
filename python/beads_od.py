"""
ID: happyn61
LANG: PYTHON3
PROB: beads
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

fin = open ('beads.in', 'r')
fout = open ('beads.out', 'w')
N=int(fin.readline().strip())
beads=list(fin.readline().strip())
print(beads)
max=0
current=0
for i in range(23,24):
    total= fwct(beads,i,1)+fwct(beads,i-1,-1)
    
    if total >= N:
        total=N
    print(i,total)
    if total > max:
        max=total
        current=i
        
print(max)

fout.write (str(max)+'\n')
    
#    print(names[i] + ' '+str(money[i])+'\n')
    
fout.close()
