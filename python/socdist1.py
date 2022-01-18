"""
ID: happyn61
LANG: PYTHON3
PROB: socdist1.py
"""

  
# Driver program to test the above functions 
fin = open ('socdist1.in', 'r')
fout = open ('socdist1.out', 'w')
#N,A,B=list(map(int,fin.readline().strip().split()))
N=int(fin.readline().strip())

from datetime import datetime
print(datetime.now())
l=[]
w=fin.readline().strip()
k=0
if w[0]=='0':
    start=True
else:
    start=False

d11=d12=0
d2m=0
kk=len(w)
for i in w:
    
    if i=='0':
        k+=1
        #print(k)
    else:
        #print(k)
        if k<1:
            continue
        if start:
            d1=k
            start=False
            d2=(k+1)//2
        else:
            d1=(k+1)//2
            d2=(k+1)//3
            kk=min(kk,k)
        if d1>=d11:
            d12=d11
            d11=d1
        elif d1>d12:
            d12=d1        
        d2m=max(d2m,d2)
        
        #print(k,d11,d12)
        k=0
print(k,d2m,d11,d12)
if k>0:
    if start:
        d2=k-1
        d1=k-1
    else:
        d1=k
        d2=(k+1)//2
    if d1>=d11:
        d12=d11
        d11=d1
    elif d1>d12:
        d12=d1        
    d2m=max(d2m,d2)
    
    k=0
    
print(d2m,d11,d12,kk)
fout.write (str(min(kk+1,max(d12,d2m)))+'\n')
print(datetime.now())

#fout.write (str(y[1])+'\n')
#fout.write (str(y[2])+'\n')
#    print(names[i] + ' '+str(money[i])+'\n')
    
fout.close()
