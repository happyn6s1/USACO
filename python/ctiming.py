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

fin = open ('ctiming.in', 'r')
fout = open ('ctiming.out', 'w')
d,h,m=map(int,fin.readline().strip().split())

x=(d-11)*24*60+(h-11)*60+(m-11)
if x<0:
    x=-1

    
fout.write (str(x)+'\n')

fout.close()
