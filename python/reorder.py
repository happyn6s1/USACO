"""
ID: happyn61
LANG: PYTHON3
PROB: reorder
"""

  
# Driver program to test the above functions 
fin = open ('reorder.in', 'r')
fout = open ('reorder.out', 'w')

from datetime import datetime
print(datetime.now())
N=int(fin.readline().strip())
A=[0]
B=[0]
C=[]
d={0:0}

for i in range(N):
    A.append(int(fin.readline().strip()))
for i in range(N):
    B.append(int(fin.readline().strip()))
    d[B[-1]]=i+1

print(A,B,d)
for i in range(len(A)):
    A[i]=d[A[i]]
print(A)
s=0
m=-1
v=[False for i in range(N+1)]
for i in range(1,len(A)):
    
    st=i
    
    
    if v[i] or i==A[st]:
        continue
    k=1
    s+=1
    v[st]=True
    while i!=A[st]:
        k+=1
        
        st=A[st]
        v[st]=True
    m=max(k,m)
    
print(s,m)
        
    
fout.write (str(s)+" "+str(m)+'\n')
#fout.write (str(y[1])+'\n')
#fout.write (str(y[2])+'\n')
#    print(names[i] + ' '+str(money[i])+'\n')
    
fout.close()
