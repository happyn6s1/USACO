"""
ID: happyn61
LANG: PYTHON3
PROB: cowmbat
"""
import collections
import sys
def traverse(node,vlist):
    #print(root)
    #print(trees[root])
    for c in vlist[node]:
        #print(c)
        nn=vls[node]
        #print(nn)
        vls[c]=vls[c].union(vls[node])
        traverse(c,vlist)

        
fin = open ('div7.in', 'r')
fout = open ('div7.out', 'w')
N=int(fin.readline().strip())



mm=0
#for each mod min and max
ma = [ [ 0 for i in range(2) ] for j in range(7) ]
#ml= [0 for j in range(N)]
pre= [0 for j in range(N+1)]
#pst= [0 for j in range(N+1)]

#print(N)
ss=0
for i in range(N):
    ml=int(fin.readline().strip())%7
    ss=(ss+ml)%7
    pre[i+1]=ss
    if ma[ss][0]==0:
        ma[ss][0]=i+1
        ma[ss][1]=i+1
    else:
        if (i+1) < ma[ss][0]:
            ma[ss][0]=i+1
        elif ma[ss][1] < (i+1):
            ma[ss][1]=i+1

for i in range(7):
    print(i)
    if ma[i][1]-ma[i][0]>mm:
        mm=ma[i][1]-ma[i][0]
        
                                   
print(mm)
fout.write (str(mm)+'\n')
fout.close()
