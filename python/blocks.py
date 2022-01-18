"""
ID: happyn61
LANG: PYTHON3
PROB: blocks
"""

fin = open ('blocks.in', 'r')
fout = open ('blocks.out', 'w')
N=int(fin.readline().strip())
l=[]
rl=[0 for i in range(26)]
d1=[0 for i in range(26)]
d2=[0 for i in range(26)]

for i in range(N):
    a,b=list(fin.readline().strip().split())
    d1=[0 for i in range(26)]
    for c in a:
        d1[ord(c)-ord('a')]+=1
        
    d2=[0 for i in range(26)]
    for c in b:
        d2[ord(c)-ord('a')]+=1
    for i in range(26):
        rl[i]+=max(d1[i],d2[i])
rr=0
print(rl)
print(rr)
for i in range(26):        
    fout.write(str(rl[i])+"\n")
                
fout.close()
    
