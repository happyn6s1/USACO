"""
ID: happyn61
LANG: PYTHON3
PROBLEM NAME: cowrace
"""
fin = open ('proximity.in', 'r')
fout = open ('proximity.out', 'w')
N,K=map(int,fin.readline().strip().split())
a=[]
b=[]
max=-1
d=dict()
print(N,K)
for i in range(0+1,N+1):
    x=int(fin.readline().strip())
   # print(x)
 #   print(i,x)
    if x in d:
        
        #print(d)
        diff=i-d[x]
        if diff < K+1:
            if x>max:
                max=x
        d[x]=i
    else:
        d[x]=i

            
print(d)
print(max)
#print(b)



#print(n2%47)
#print(n)
fout.write (str(max) + '\n')
fout.close()
