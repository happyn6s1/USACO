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
bstr=fin.readline().strip()
beads=list(bstr)
#beads.reverse()
print(beads)
max=0
current=0
color='w'
start=False
k=0
cw=0
for i in range(N):
    print(i,beads[i])
    #total= fwct(beads,i,1)+fwct(beads,i-1,-1)
    if beads[i]=='w':
        cw=cw+1
        continue
    if color=='w':
        color=beads[i]
        cw=0
        continue
    if color==beads[i]:
        cw=0
        continue
    else:
        k=i
        break


rl=[0]*N
ll=[0]*N
#print(rl,ll)
print(k,cw,beads[k],N)

    
ct=cw
color='w'
for i in range(N):
    index=(k+i)%N
#    print(index)
#    print(color,beads[index])
    if beads[index]=='w':
        cw=cw+1
        ct=ct+1
    elif color=='w':
        color=beads[index]
        cw=0
        ct=ct+1
    elif color==beads[index]:
        cw=0
        ct=ct+1
    else:
        ct=cw+1
        cw=0
        color=beads[index]
    rl[index]=ct
print(rl)
ct=0
color='w'
for i in range(N):
    index=(k-1-i)%N
#    print(index)
#    print(color,beads[index])
    if beads[index]=='w':
        ct=ct+1
    elif color=='w':
        color=beads[index]
        ct=ct+1
    elif color==beads[index]:
        ct=ct+1
    else:
        ct=1
        color=beads[index]
    i2=(index-1)%N
    ll[index]=ct+rl[i2]
 #   ll[i2]=rl[index]+ct
    if ll[index]>max:
        max=ll[index]
print(rl)
print(ll)


if k == 0 or max>N:
    max=N
print(max)

fout.write (str(max)+'\n')
    
#    print(names[i] + ' '+str(money[i])+'\n')
    
fout.close()
