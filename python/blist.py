"""
ID: happyn61
LANG: PYTHON3
PROB: friday
"""


fin = open ('blist.in', 'r')
fout = open ('blist.out', 'w')

cowlist=[]
n=int(fin.readline().strip())
eachcow=[0,0,0]
for i in range(n):
    eachcow=list(map(int,fin.readline().strip().split()))
    cowlist.append(eachcow)

print(cowlist)
cowlist.sort()
print(cowlist)

smax=0
for i in range(1,1000):
    s=0
    for j in cowlist:
        if i in range(j[0],j[1]+1):
            s+=j[2]
    if s>smax:
        smax=s

print(smax)
fout.write (str(smax)+'\n')
#fout.write (str(y[1])+'\n')
#fout.write (str(y[2])+'\n')
#    print(names[i] + ' '+str(money[i])+'\n')
    
fout.close()
