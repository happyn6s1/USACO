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

fin = open ('planting.in', 'r')
fout = open ('planting.out', 'w')
n=int(fin.readline().strip())
t=0
color=1
conn=[[] for i in range(n+1)]
conn2=[[] for i in range(n+1)]
degree=[0]*(n+1)
for i in range(n-1):
    l=list(map(int,fin.readline().strip().split()))
    degree[l[0]]+=1
    degree[l[1]]+=1
    conn[l[0]].append(l[1])
    conn[l[1]].append(l[0])
#print(degree)
#print(ddegree)
t=max(degree)+1
print(t)
fout.write (str(t)+'\n')

fout.close()
