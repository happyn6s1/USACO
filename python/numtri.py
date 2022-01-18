"""
ID: happyn61
LANG: PYTHON3
PROB: numtri
"""

#from collections import defaultdict

#import heapq

fin = open ('numtri.in', 'r')
fout = open ('numtri.out', 'w')
#print(dic["4734"])
R=int(fin.readline().strip())


mm=0
ll=[]
nl=[]

setr=set()
for i in range(R):
    t=[int(i) for i in fin.readline().strip().split()]
    ll.append(t)
    tt=t.copy()
    mm=0
    if i>0:
        for j in range(i+1):
            print(i,j)
            if j == 0:
                tt[j]=nl[i-1][j]+tt[j]
            elif j==i:
                tt[j]=nl[i-1][j-1]+tt[j]
            else:
                
                tt[j]+=max(nl[i-1][j-1],nl[i-1][j])
            if tt[j]>mm:
                mm=tt[j]
            
        nl.append(tt)
    else:
        nl.append(ll[i])
        mm=ll[i][0]
    
print(mm)
print(ll,nl)
fout.write (str(mm)+"\n")
fout.close()
