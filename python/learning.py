"""
ID: happyn61
LANG: PYTHON3
PROB: learning.py
"""

  
# Driver program to test the above functions 
fin = open ('learning.in', 'r')
fout = open ('learning.out', 'w')
N,A,B=list(map(int,fin.readline().strip().split()))
from datetime import datetime
print(datetime.now())
l=[]
for i in range(N):
    s,w=fin.readline().strip().split()
    w=int(w)
    l.append([w,s])
l.sort()
#print(l)
ll=[]
lll=[]
for i in range(1,N):
    if l[i][0]<A:
        continue
    if l[i][1]!=l[i-1][1]:
        ll.append([l[i-1][0],l[i][0],l[i][1]])
        if l[i-1][1]=="S":
            lll.append(("S1",(l[i-1][0]+l[i][0])//2))
            #lll.append(("NS0",(l[i-1][0]+l[i][0])//2+1))
            
        else:
            #lll.append(("NS1",(l[i-1][0]+l[i][0]-1)//2))
            lll.append(("S0",(l[i-1][0]+l[i][0]-1)//2+1))
        if l[i][0]>B:
            break
k=0
#print(ll)
#print(lll)
ss=[]

for i in lll:
    if i[0]=='S0':
        ss.append(i[1])
    #if i[0]=='NS0':
    #    ns.append(i[1])
    if i[0]=='S1':
        if len(ss)>0:
            j=ss.pop()
        else:
            j=A
        if j<A:
            j=A
        if i[1]>B:
            k+=(B-j+1)
        elif (i[1]-j+1)>0:
            k+=(i[1]-j+1)
    #if i[0]=='NS1':
    #    pass
if ss and (B-ss[-1]+1)>0:
    k+=(B-ss.pop()+1)
print(k)
fout.write (str(k)+'\n')
print(datetime.now())

#fout.write (str(y[1])+'\n')
#fout.write (str(y[2])+'\n')
#    print(names[i] + ' '+str(money[i])+'\n')
    
fout.close()
