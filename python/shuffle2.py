"""
ID: happyn61
LANG: PYTHON3
PROB: pump
"""

from collections import defaultdict

import heapq

fin = open ('shuffle.in', 'r')
fout = open ('shuffle.out', 'w')
#print(dic["4734"])
N=int(fin.readline().strip())
sl=fin.readline().strip().split()
si=[]
sii={}
ss=0
sset=set()
for i in range(1,N+1):
    #si.append(int(sl[i]))
    sii[i]=[int(sl[i-1]),N+1]
    #ss+=int(sl[i])
    sset.add(i)
#sii.sort()
print(sii,sset)


mm=0
aa=0
j=0
while sii:
    i=sii.keys()[0]
    #print(i)
    if sii[i][0]==i:
        
        mm+=1
        del sii[i]
    else:
        j=i
        sii[i][1]=i
        j=sii[i][0]
        while sii[j][0] in sii.keys():
            if sii[sii[j][0]][1] ==i:
                sii[sii[j][0]][1] =0
                mm+=1
                j=sii[j][0]
                del sii[j]
            else:
                
                sii[sii[j][0]][1] = i
                j=sii[j][0]
            if j not in sii.keys():
                break
            #print(j, sii[j][0])
            
            
        #print(i,aa,mm,"+")
#print(flist)

        
#print(sii)  
print(mm)

fout.write (str(mm)+'\n')
fout.close()
