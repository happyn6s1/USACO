"""
ID: happyn61
LANG: PYTHON3
PROB: frac1
"""
def coprime(n,m):
	while n>1 and m>1 and n!=m:
		if n>m:
			n=n-m
		else:
			m=m-n
	if n==1 or m==1:
		return True
	else:
		return False
	    

fin = open ('frac1.in', 'r')
fout = open ('frac1.out', 'w')
ns=[[0,1],[1,1]]
N = int(fin.readline().strip())

def merge(n,l):
    mm=[]
    i=0
    j=0
    while i < len(n) and j<len(l):
        if n[i][0]*l[j][1]>n[i][1]*l[j][0]:
            mm.append(l[j])
            j+=1
        else:
            mm.append(n[i])
            i+=1
    while i<len(n):
        mm.append(n[i])
        i+=1
    while j<len(l):
        mm.append(l[j])
        j+=1
    return mm
        
for i in range(2,N+1):
    ll=[]
    for j in range(1,i):
        if coprime(i,j):
            ll.append([j,i])

    ns=merge(ns,ll)
            
#print(ns)
for i in range(len(ns)):
    fout.write(str(ns[i][0])+"/"+str(ns[i][1])+"\n")
                
fout.close()
