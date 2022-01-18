"""
ID: happyn61
LANG: PYTHON3
PROB: milk2
"""


fin = open ('milk2.in', 'r')
fout = open ('milk2.out', 'w')
N=int(fin.readline().strip())
ml=[]
for i in range(N):
    it=fin.readline().strip().split()
    print(it)
    ml.append(int(it[0])*2)
    ml.append(int(it[1])*2+1)
ml.sort()

mv=0 #0
mav=0 #1
ct=0
flag=-1
last=0
print(ml)
for i in range(2*N):
    if(ml[i]%2==0):
        ct+=1
    else:
        ct-=1
    print(i,ml[i],ct,flag,last)
    if ct==1 and flag<=0:
        flag=1
        if ml[i]-ml[last]>mv:
            mv=ml[i]-ml[last]
        last=i
    if ct==0 and flag==1:
        flag=0
        if ml[i]-ml[last]>mav:
            mav=ml[i]-ml[last]
        last=i
    print(mav,mv)
print(mav//2,(mv+1)//2)
max=0
fout.write (str(mav//2)+" "+str((mv+1)//2)+'\n')
    
#    print(names[i] + ' '+str(money[i])+'\n')
    
fout.close()
