"""
ID: happyn61
LANG: PYTHON3
PROB: angry
"""

  
# Driver program to test the above functions 
fin = open ('angry.in', 'r')
fout = open ('angry.out', 'w')

from datetime import datetime
print(datetime.now())
N=int(fin.readline().strip())
l=[]
for i in range(N):
    l.append(int(fin.readline().strip()))
l.sort()

m=(l[-1]-l[0])

la=[0 for i in range(N)]
lb=[0 for i in range(N)]
for i in range(1,N):
    la[i]=max(l[i]-l[i-1],la[i-1])
    lb[N-1-i]=max(l[N-i]-l[N-i-1],lb[N-i])

for i in range(1,N):
    
    if la[i-1]+lb[i]>=((l[i]-l[i-1])/2):
        
        m=min(m,max(la[i-1],lb[i])+1)
    else:
        m=min(m,(l[i]-l[i-1])/2)
    m=min(m,max(la[i],lb[i]))
    #print(m)
m=min(m,max(la[0],lb[0]))
print(m*1.0)
fout.write (str(m*1.0)+'\n')
#fout.write (str(y[1])+'\n')
#fout.write (str(y[2])+'\n')
#    print(names[i] + ' '+str(money[i])+'\n')
    
fout.close()
