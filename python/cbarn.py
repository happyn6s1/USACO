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

        
fin = open ('cbarn.in', 'r')
fout = open ('cbarn.out', 'w')
N=int(fin.readline().strip())



mm=0
#for each mod min and max
#ma = [ [ 0 for i in range(2) ] for j in range(7) ]
ml= [int(fin.readline().strip()) for j in range(N)]
p= [0 for j in range(N)]
#pst= [0 for j in range(N+1)]

#print(N)

ss=0
nn=99999
nnn=-1
for i in range(N):
    ss+=(ml[i]-1)
    p[i]=ss
    if ss<=nn:
        nn=ss
        nnn=i
    
print(p,nn,nnn)
nl=[]
for i in range(N):
    j=(i+nnn+1)%N #offsit
    #print(ml[j])
    for k in range(ml[j]):
        nl.append(i)
for i in range(N):
    mm+=(nl[i]-i)**2
print(nl)
'''
    ml=int(fin.readline().strip())
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
'''
print(ml)

                                   
print(mm)
fout.write (str(mm)+'\n')
fout.close()
