"""
ID: happyn61
LANG: PYTHON3
PROB: friday
"""
def overlaps(x1,x2,x3,x4):
    if x1 < x3:
        xstart=x1
    else:
        xstart=x3
    if x2 > x4:
        xend=x2
    else:
        xend=x4
    overx=(x2-x1)+(x4-x3)-(xend-xstart)
    if overx<0:
        overx=0
    return overx

fin = open ('paint.in', 'r')
fout = open ('paint.out', 'w')
b1=fin.readline().strip().split()
b2=fin.readline().strip().split()
o1=overlaps(int(b1[0]),int(b1[1]),int(b2[0]),int(b2[1]))    
a=(int(b1[1])-int(b1[0]))+(int(b2[1])-int(b2[0]))
print(a-o1)
fout.write (str(a-o1)+'\n')

fout.close()
