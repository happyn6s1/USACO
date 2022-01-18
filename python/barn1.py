"""
ID: happyn61
LANG: PYTHON3
PROB: barn1
"""

#from collections import defaultdict

#import heapq

fin = open ('barn1.in', 'r')
fout = open ('barn1.out', 'w')
#print(dic["4734"])
NSC=(fin.readline().strip().split())
M=int(NSC[0])
S=int(NSC[1])
C=int(NSC[2])

nl=[]
nd=[]
#nl=[[0,-1] for i in range(N)]
ss=0

for i in range(C):
    oc=int(fin.readline().strip())
    
    nl.append(oc)
nl.sort()
for i in range(C):
    if i>0:
        nd.append(nl[i]-nl[i-1]-1)
        
dd=nl[C-1]-nl[0]+1
print(dd)
nd.sort(reverse=True)
tt=0
print(nl,nd,S,dd)
for i in range(M-1):
    if M>C:
        dd=C
        break
    dd-=nd[i]
   
mm=dd    
print(dd)
fout.write (str(mm)+'\n')
fout.close()
