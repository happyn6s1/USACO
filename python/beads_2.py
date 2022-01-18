"""
ID: happyn61
LANG: PYTHON3
PROB: beads
"""
def fwct(lo,i,step):
    l=lo.copy()
    color=l[i]
    n=i%N
    c=0
    print(l[n])
    while (l[n]=='w' or l[n] == color) and l[n]!='d' :
        n=(n+step)%N
        
        c=c+1
        if color =='w' and l[n] != color:
            color=l[n]
        print(n,color)
        l[n]='d'
    print(c)
    return c

fin = open ('beads.in', 'r')
fout = open ('beads.out', 'w')
N=int(fin.readline().strip())
bstr=fin.readline().strip()
beads=list(bstr+bstr)
max=0
current=0
fwd=[]
total=0
for i in range(N*2):
    #total= fwct(beads,i,1)+fwct(beads,i-1,-1)
    if beads[i] <> 'w':
        if beads[i] == currentcolor or currentcolor='w':
        else:
            
    elif i<N:
        total=total+1
        max=N
        break
    
    print(i,total)
    if total == N*2:
        total=N
    if total > max:
        max=total
        current=i
        
print(max)

fout.write (str(max)+'\n')
    
#    print(names[i] + ' '+str(money[i])+'\n')
    
fout.close()
