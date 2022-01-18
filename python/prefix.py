"""
ID: happyn61
LANG: PYTHON3
PROB: prefix
"""

fin = open ('prefix.in', 'r')
fout = open ('prefix.out', 'w')

p=[]
ip= fin.readline().strip().split()
while ip[0]!='.':
    p=p+ip
    ip= fin.readline().strip().split()

ml=0
for i in p:
    ml=max(ml,len(i))
s=""
ss=fin.readline().strip()
while ss:
    s=s+ss
    ss=fin.readline().strip()
ps=set(p)
#print(ps,s,ml)
le=len(s)
ll=[-1]*(le+1)
ll[0]=0
rr=0
print(ml,le)
for i in range(le):
    ii=i+1
    for j in range(ml):
        jj=j+1
        if ii-jj>=0 and s[ii-jj:ii] in ps and ll[ii-jj]>=0:
            ll[ii]=max(ll[ii],1+ll[ii-jj])
            break
    if ll[ii]>0:
        rr=ii
#print(ll,rr)
#fout.write("IMPOSSIBLE"+"\n")
#print(r)
fout.write(str(rr)+"\n")
                
fout.close()
    
