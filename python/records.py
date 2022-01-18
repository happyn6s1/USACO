"""
ID: happyn61
LANG: PYTHON3
PROB: friday
"""
def compare(comb,key):
    for i in range(3):
        if abs(comb[i]-key[i])<=2 or abs(comb[i]-key[i])>=48:
            continue
        else:
            return False
        
                                         
    return True

fin = open ('records.in', 'r')
fout = open ('records.out', 'w')
n=int(fin.readline().strip())
print(n)
t=0
fwd=[0]
d=dict()
for i in range(n):
    m=fin.readline().strip().split()
    m.sort()
    mm=m[0]+"="+m[1]+"="+m[2]
    if mm not in d:
        d[mm]=1
    else:
        d[mm]+=1
print(d)
t=0

for key in d:
    if d[key] >t:
        t=d[key]
print(t)
fout.write (str(t)+'\n')

fout.close()
