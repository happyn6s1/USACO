"""
ID: happyn61
LANG: PYTHON3
PROB: speeding
"""

fin = open ('speeding.in', 'r')
fout = open ('speeding.out', 'w')

p=[]
N,M= list(map(int,fin.readline().strip().split()))

nl=[[0,0]]
for i in range(N):
    a,b=list(map(int,fin.readline().strip().split()))
    nl[i][1]=b
    nl.append([nl[i][0]+a,0])

ml=[[0,0]]
for i in range(M):
    a,b=list(map(int,fin.readline().strip().split()))
    ml[i][1]=b
    ml.append([ml[i][0]+a,0])
print(nl,ml)
rr=0
i=j=0

while i<N and j<M:
    print(nl[i],ml[j])
    rr=max(rr,ml[j][1]-nl[i][1])
    if ml[j+1][0]>nl[i+1][0]:
        i+=1
    elif ml[j+1][0]==nl[i+1][0]:
        i+=1
        j+=1
        
    else:
        j+=1
print(rr)
        
fout.write(str(rr)+"\n")
                
fout.close()
    
