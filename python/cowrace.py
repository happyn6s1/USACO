"""
ID: happyn61
LANG: PYTHON3
PROBLEM NAME: cowrace
"""
fin = open ('cowrace.in', 'r')
fout = open ('cowrace.out', 'w')

M,N=map(int,fin.readline().strip().split())
print(M)
print(N)
a=[]
b=[]
for i in range(0,M):
    x,y=map(int,fin.readline().strip().split())
#    print(x,y)
    for n in range(0,y):
        a.append(x)
        
for i in range(0,N):
    x,y=map(int,fin.readline().strip().split())
#    print(x,y)
    for n in range(0,y):
        b.append(x)
            
#print(a)
#print(b)

n=0
A=0
B=0
w=''
for i in range(0,len(a)):
    A=A+a[i]
    B=B+b[i]
 #   print(A,B)
    if A>B:
        if(w=='B'):
            n=n+1
        w='A'
 #       print(A,B,n)
    if B>A:
        if w=='A':
            n=n+1
        w='B'
 #       print(A,B,n)

#print(n2%47)
#print(n)
fout.write (str(n) + '\n')
fout.close()
