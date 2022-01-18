"""
ID: happyn61
LANG: PYTHON3
PROB: fracdec
"""
import collections
import sys
     
fin = open ('fracdec.in', 'r')
fout = open ('fracdec.out', 'w')
NM=fin.readline().strip().split()
N=int(NM[0])
D=int(NM[1])
h=0
r=N
if N>=D:
    h=N//D
    r=N%D
c=0
l=[]
s={}
i=0
j=-1
rec=False
while r>0:
    r=r*10
    c=r//D
    r=r%D
    if (c,r) not in s:
        l.append(str(c))
        s[(c,r)]=i
        
    else:
        j=s[(c,r)]
        rec=True
        break
    i+=1
#print(l,i,j,s)
if not rec:
    if len(l)==0:
        a=str(h)+".0"
    else:
        a=str(h)+"."+"".join(l)
   
else:
    a=str(h)+"."+"".join(l[:j])+"("+"".join(l[j:i])+")"
#print(a)

lll=len(a)
lines=lll//76
r=lll%76
for i in range(lines):
    fout.write (a[i*76:(i+1)*76] + '\n')
fout.write (a[-r:] + '\n')

fout.close()
