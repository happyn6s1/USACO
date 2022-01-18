"""
ID: happyn61
LANG: PYTHON3
PROB: crosswords
"""

  
# Driver program to test the above functions 
fin = open ('crosswords.in', 'r')
fout = open ('crosswords.out', 'w')

from datetime import datetime
print(datetime.now())
r,c=list(map(int,fin.readline().strip().split()))
m=[]
for i in range(r):
    m.append(list(fin.readline().strip()))
#print(m)
l=[]
k=0
for i in range(r):
    cc=0
    for j in range(c-1,-1,-1):
        if m[i][j]==".":
            cc+=1
        else:
            if cc>=3:
                k+=1
                l.append((i,j+1))
            cc=0
    if cc>2 and m[i][0]=='.':
        k+=1
        l.append((i,0))
    #print(i,j,m[i][j],cc,l)
for j in range(c):
    cc=0
    for i in range(r-1,-1,-1):
        
        if m[i][j]==".":
            cc+=1
        else:
            
            if cc>=3:
                k+=1
                l.append((i+1,j))
            cc=0
    if cc>2 and m[0][j]=='.':
        k+=1
        l.append((0,j))
    #print(i,j,m[i][j],cc,l)
ll=list(set(l))
ll.sort()
nn=len(ll)
fout.write (str(nn)+'\n')
for i in range(nn):
    fout.write (str(ll[i][0]+1)+' '+str(ll[i][1]+1)+'\n')
#fout.write (str(y[1])+'\n')
#fout.write (str(y[2])+'\n')
#    print(names[i] + ' '+str(money[i])+'\n')
    
fout.close()
