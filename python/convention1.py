"""
ID: happyn61
LANG: PYTHON3
PROB: barn1
"""

#from collections import defaultdict

#import heapq

fin = open ('convention.in', 'r')
fout = open ('convention.out', 'w')
#print(dic["4734"])
NMC=fin.readline().strip().split()
N=int(NMC[0])
M=int(NMC[1])
C=int(NMC[2])

nl=[]
nd=[]
#nl=[[0,-1] for i in range(N)]
ss=0

nl=fin.readline().strip().split()
for i in range(len(nl)):
    nl[i]=int(nl[i])
    

nl.sort()
print(nl,N,M,C)
def check(w):
    i=0
    for j in range(M): #loop each bus
        b=nl[i]
        t=C-1
        i+=1
        while t>0 and i<len(nl) and nl[i]-b<=w:
            i+=1
            t-=1
        if i>=len(nl):
            return True
    return False
        
mm=0
print(mm)
nd.sort(reverse=True)
tt=0
lo=0
hi=nl[-1]-nl[0]
ans=-1
while lo<=hi:
    mi=(lo+hi)//2
    if check(mi):
        hi=mi-1
        ans=mi
    else:
        lo=mi+1
print(ans)
fout.write (str(ans)+'\n')
fout.close()
