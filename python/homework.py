"""
ID: happyn61
LANG: PYTHON3
PROB: pump
"""

from collections import defaultdict

import heapq

fin = open ('homework.in', 'r')
fout = open ('homework.out', 'w')
#print(dic["4734"])
N=int(fin.readline().strip())
sl=fin.readline().strip().split()
si=[]
sii=[]
ss=0

for i in range(N):
    si.append(int(sl[i]))
    sii.append([int(sl[i]),i])
    ss+=int(sl[i])
sii.sort()
print(si,ss,sii)

mm=[]
aa=0
j=0
for i in range(0,N-2):
    if si[i]==sii[j][0]:
        j+=1
    ss-=si[i]
    if (ss-sii[j][0])/(N-i-2)==aa:
        mm.append(i+1)
        #print(i,aa,mm)
    elif (ss-sii[j][0])/(N-i-2)>aa:
        mm=[]
        mm.append(i+1)
        aa=(ss-sii[j][0])/(N-i-2)
        #print(i,aa,mm,"+")
#print(flist)

  
print(mm)
for i in mm:
    fout.write (str(i)+'\n')
fout.close()
