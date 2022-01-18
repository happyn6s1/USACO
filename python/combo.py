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

fin = open ('combo.in', 'r')
fout = open ('combo.out', 'w')
n=int(fin.readline().strip())
farmer=list(map(int,fin.readline().strip().split()))
master=list(map(int,fin.readline().strip().split()))

print(farmer,master,n)
m=1
for i in range(3):
    k=abs(farmer[i]-master[i])
    if k>n//2:
        k=n-k
    if k<=4:
        m=m*(5-k)
    else:
        m=0

print(250-m)                
fout.write (str(250-m)+'\n')

fout.close()
