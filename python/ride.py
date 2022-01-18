"""
ID: happyn61
LANG: PYTHON3
PROG: ride
"""
fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')
l1=fin.readline()
l2=fin.readline()
n1=1
n2=1
for n in l1:
    if ord(n)<60:
        break
    #print(str(ord(n)-64)+n)
    n1=n1*(ord(n)-64)
for n in l2:    
    if ord(n)<60:
        break
    n2=n2*(ord(n)-64)

if (n1%47)==(n2%47):
    fout.write ("GO" + '\n')
else:
    fout.write("STAY" + '\n')
    
#print(n1%47)
#print(n2%47)
#fout.write (str(sum) + '\n')
fout.close()
