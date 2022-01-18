"""
ID: happyn61
LANG: PYTHON3
PROB: pump
"""

#from collections import defaultdict

#import heapq

fin = open ('revegetate.in', 'r')
fout = open ('revegetate.out', 'w')
#print(dic["4734"])
NM=(fin.readline().strip().split())
N=int(NM[0])
M=int(NM[1])
    
nl=[[0,-1] for i in range(N)]
ss=0

for i in range(M):
    SD=(fin.readline().strip().split())
    if 
    #si.append(int(sl[i]))
    sii.append([int(sl[i-1]),N+1])
    #ss+=int(sl[i])
#sii.sort()
#print(sii)

nn=0
mm=0
aa=0
j=0
for i in range(1,N+1):
    #print(i,sii[i],nn)
    if sii[i][1]<N+1:
        continue

    if sii[i][0]==i:
        sii[i][1]=0
        mm+=1
    else:
        #print(sii[i],sii[sii[j][0]])
        j=i
        sii[i][1]=i
        
        while sii[sii[j][0]][1] !=0:
            if sii[sii[j][0]][1] ==i:
                sii[sii[j][0]][1] =0
                mm+=1
            elif sii[sii[j][0]][1] < i:
                break
            else:
                sii[sii[j][0]][1] = i
            j=sii[j][0]
            nn+=1
            #print(i,sii[j][0],sii[sii[j][0]],nn)
        #print(mm)
        #print(i,aa,mm,"+")
#print(flist)

        
#print(sii)  
print(mm)
print(nn)
fout.write (str(mm)+'\n')
fout.close()
