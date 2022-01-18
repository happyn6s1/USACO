"""
ID: happyn61
LANG: PYTHON3
PROB: hoofball
"""

#from collections import defaultdict

import heapq

fin = open ('hoofball.in', 'r')
fout = open ('hoofball.out', 'w')
#print(dic["4734"])
NK=fin.readline().strip().split()
n=int(NK[0])
K=int(NK[1])
l=[]
for i in range(n):
    l.append(int(fin.readline().strip()))
l.sort()
h=[]
ans=0
def check(w):
    t=K
    lead=-99999999999
    for i in range(n):
        if l[i]-lead>2*w:
            t-=1
            lead=l[i]
            if t<0:
                return False
    return True

lo=0
hi=l[-1]-l[0]
ans=hi
while lo<=hi:
    mi=(lo+hi)//2
    if check(mi):
        ans=mi
        hi=mi-1
    else:
        lo=mi+1
print(ans)
fout.write (str(ans)+'\n')
fout.close()
