"""
ID: happyn61
LANG: PYTHON3
PROB: feast
"""

  
# Driver program to test the above functions 
fin = open ('feast.in', 'r')
fout = open ('feast.out', 'w')

from datetime import datetime
print(datetime.now())
T,A,B=list(map(int,fin.readline().strip().split()))
m=0
l=[False for i in range(T+1)]
l[0]=l[A//2]=l[B//2]=True
if (A+B)<T:
    l[(A+B)//2]=True

for i in range(T+1):
    if l[i]:
        m=max(m,i)
    else:
        if i-A>=0 and l[i-A]:
            l[i]=True
            m=max(m,i)
        elif i-B>=0 and l[i-B]:
            l[i]=True
            m=max(m,i)
print(m)

for i in range(T+1):
    if l[i]:
        print(i)
fout.write (str(m)+'\n')
#fout.write (str(y[1])+'\n')
#fout.write (str(y[2])+'\n')
#    print(names[i] + ' '+str(money[i])+'\n')
    
fout.close()
