"""
ID: happyn61
LANG: PYTHON3
PROB: friday
"""

fin = open ('convention.in', 'r')
fout = open ('convention.out', 'w')

m,n,c=map(int,fin.readline().strip().split())
arr=list(map(int,fin.readline().strip().split()))
arr.sort()
limit=c

s=[]
for i in range(m-1):
    s.append(arr[i+1]-arr[i])
print(s)

s.sort()

print(s)
fout.write (str(s[n])+'\n')
#fout.write (str(y[1])+'\n')
#fout.write (str(y[2])+'\n')
#    print(names[i] + ' '+str(money[i])+'\n')
    
fout.close()
