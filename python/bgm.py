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

        
fin = open ('bgm.in', 'r')
fout = open ('bgm.out', 'w')
N=int(fin.readline().strip())
strl=list("BESIGOM")


mm=0
ma = [ [ 0 for i in range(7) ] for j in strl ]

print(N)
for i in range(N):
    AB=fin.readline().strip().split()
    ma[strl.index(AB[0])][int(AB[1])%7]+=1
print(ma)
for bi in range(7):
    for ei in range(7):
        for si in range(7):
            for ii in range(7):
                for gi in range(7):
                    for oi in range(7):
                        for mi in range(7):
                          
                            if (bi+ei+si+si+ii+ei) % 7 ==0 or (gi+oi+ei+si)%7==0 or (mi+oi+oi)%7==0:
                                
                                mm+=ma[0][bi]*ma[1][ei]*ma[2][si]*ma[3][ii]*ma[4][gi]*ma[5][oi]*ma[6][mi]
                                    
print(mm)
fout.write (str(mm)+'\n')
fout.close()
