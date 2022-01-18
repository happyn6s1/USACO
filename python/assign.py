"""
ID: happyn61
LANG: PYTHON3
PROBLEM NAME: assign
"""


fin = open ('assign.in', 'r')
fout = open ('assign.out', 'w')
N,K=map(int,fin.readline().strip().split())
#same list of sets
s=[set() for _ in range(N)]
d=[set() for _ in range(N)]
print(N,K)
for i in range(0+1,K+1):
    a,b,c=fin.readline().strip().split()


    if a == 'S':
        s[b].add(c)
        s[c].add(b)

    if a == 'D':
        d[b].add(c)
        d[c].add(b)
   # print(x)
 #   print(i,x)
print(s)
print(d)

    


#print(n2%47)
#print(n)
fout.write (str(max) + '\n')
fout.close()
