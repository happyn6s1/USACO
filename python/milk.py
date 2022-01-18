"""
ID: happyn61
LANG: PYTHON3
PROB: milk
"""

#from collections import defaultdict

#import heapq

fin = open ('milk.in', 'r')
fout = open ('milk.out', 'w')
#print(dic["4734"])
NM=(fin.readline().strip().split())
M=int(NM[0])
N=int(NM[1])
nl=[]    
#nl=[[0,-1] for i in range(N)]
ss=0

for i in range(N):
    SD=(fin.readline().strip().split())
    S=int(SD[0])
    D=int(SD[1])
    nl.append([S,D])

nl.sort()
tt=0
i=0
while M>0:
    if nl[i][1]>M:
        
        tt+=nl[i][0]*M
        M=0
        #print(tt)
    else:
        M-=nl[i][1]
        tt+=nl[i][0]*nl[i][1]
        #print(tt,nl[i],M)
    i+=1
print(tt)
mm=tt
fout.write (str(mm)+'\n')
fout.close()
