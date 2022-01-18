"""
ID: happyn61
LANG: PYTHON3
PROB: sort3
"""

	    

fin = open ('sort3.in', 'r')
fout = open ('sort3.out', 'w')
nl=[]
ns=[]
N = int(fin.readline().strip())

for i in range(N):
    nl.append(int(fin.readline().strip()))

ns=nl.copy()
ns.sort()

a=0
b=0
for i in range(N):
    if ns[i]==nl[i]:
        continue
    if (ns[i]-nl[i]) % 3 ==1:
        a+=1
    if (ns[i]-nl[i]) % 3 ==2:
        b+=1

c=max(a,b)
d=min(a,b)

print(2*(c-d)//3+d)
fout.write(str(2*(c-d)//3+d)+"\n")
                
fout.close()
    
