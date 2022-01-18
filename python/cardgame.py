"""
ID: happyn61
LANG: PYTHON3
PROB: cardgame
"""

  
# Driver program to test the above functions 
fin = open ('cardgame.in', 'r')
fout = open ('cardgame.out', 'w')

from datetime import datetime
print(datetime.now())
N=int(fin.readline().strip())

s=set([i+1 for i in range(N*2)])
#print(s)
la=[]

for i in range(N//2):
    n=int(fin.readline().strip())
    
    s.remove(n)
    la.append(n)
lb=[]
for i in range(N//2,N):
    
    n=int(fin.readline().strip())
    s.remove(n)
    lb.append(n)

la.sort()
lb.sort()
lc=list(s)
lc.sort()
print(la)
print(lb)
print(lc)
r=0
i=N-1
j=N//2-1
#print(lc)
while i>=N//2 and j>=0:
    #print(i,j)
    if lc[i]>la[j]:
        #print(lc[i],la[j])
        r+=1
        i-=1
        j-=1
    else:
        j-=1
print(r)
i=0
j=0
while i<N//2 and j<N//2:
    if lc[i]<lb[j]:
        #print(lc[i],lb[j])
        r+=1
        i+=1
        j+=1
    else:
        j+=1
        


print(r)
fout.write (str(r)+'\n')
#fout.write (str(y[1])+'\n')
#fout.write (str(y[2])+'\n')
#    print(names[i] + ' '+str(money[i])+'\n')
    
fout.close()
