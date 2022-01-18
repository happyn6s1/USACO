"""
ID: happyn61
LANG: PYTHON3
PROB: friday
"""
def overlaps(x1,y1,x2,y2,x3,y3,x4,y4):
    if x1 < x3:
        xstart=x1
    else:
        xstart=x3
    if x2 > x4:
        xend=x2
    else:
        xend=x4
    overx=(x2-x1)+(x4-x3)-(xend-xstart)
    #print(overx)
    if overx<0:
        overx=0
    if y1 < y3:
        ystart=y1
    else:
        ystart=y3
    if y2 > y4:
        yend=y2
    else:
        yend=y4
    overy=(y2-y1)+(y4-y3)-(yend-ystart)
    #print(overy,yend,ystart)
    if overy<0:
        overy=0
    return overx*overy

fin = open ('billboard.in', 'r')
fout = open ('billboard.out', 'w')
b1=fin.readline().strip().split()
b2=fin.readline().strip().split()
c=fin.readline().strip().split()
o1=overlaps(int(c[0]),int(c[1]),int(c[2]),int(c[3]),int(b2[0]),int(b2[1]),int(b2[2]),int(b2[3]))    
o2=overlaps(int(b1[0]),int(b1[1]),int(b1[2]),int(b1[3]),int(c[0]),int(c[1]),int(c[2]),int(c[3]))    
a1=(int(b1[2])-int(b1[0]))*(int(b1[3])-int(b1[1]))
a2=(int(b2[2])-int(b2[0]))*(int(b2[3])-int(b2[1]))
#print(a1+a2-o1-o2)
fout.write (str(a1+a2-o1-o2)+'\n')

fout.close()
