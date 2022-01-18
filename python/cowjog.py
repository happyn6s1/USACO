"""
ID: happyn61
LANG: PYTHON3
PROB: cowjog.py
"""

  
# Driver program to test the above functions 
fin = open ('cowjog.in', 'r')
fout = open ('cowjog.out', 'w')
N=int(fin.readline().strip())
from datetime import datetime
print(datetime.now())
l=[0 for i in range(N)]
for i in range(N):
    r,c=list(map(int,fin.readline().strip().split()))
    l[N-1-i]=c
k=1
m=l[0]
for i in range(1,N):
    if l[i]<=m:
        m=l[i]
        k+=1
print(k)
fout.write (str(k)+'\n')

#fout.write (str(y[1])+'\n')
#fout.write (str(y[2])+'\n')
#    print(names[i] + ' '+str(money[i])+'\n')
    
fout.close()
