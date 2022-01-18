"""
ID: happyn61
LANG: PYTHON3
PROB: badmilk
"""

fin = open ('badmilk.in', 'r')
fout = open ('badmilk.out', 'w')

N,M,D,S= list(map(int,fin.readline().strip().split()))

nl=[[] for i in range(N+1)]
ml=[[] for i in range(M+1)]
for i in range(D):
    p,m,t=list(map(int,fin.readline().strip().split()))
    nl[p].append((t,m))
    ml[m].append(p)
print(nl,ml)
sl=[]
sick=set()
for i in range(S):
    ss=set()
    p,t=list(map(int,fin.readline().strip().split()))
    #sick.add(p)
    for j in nl[p]:
        if j[0]<t:
            ss.add(j[1])
    sl.append(ss)
s=sl[0]
for i in range(1,len(sl)):
    s=s.intersection(sl[i])
print(s)
for i in s:
    for j in ml[i]:
        sick.add(j)

rr=len(sick)
print(rr)
        
fout.write(str(rr)+"\n")
                
fout.close()
    
