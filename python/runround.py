"""
ID: happyn61
LANG: PYTHON3
PROB: runround
"""

def isRunround(M):
    l=[]
    while M>0:
        l.append(M % 10)
        M=M//10
    lm=[]
    l.reverse()
    ss=set()
    s=set()
    #print(l)
    ii=0
    for i in range(len(l)):
        kk=l[ii]
        #print(kk)
        if kk in s or kk==0:
            return False
        else:
            s.add(kk)
            ii=(ii+kk)%len(l)
            #print(s)
    kk=l[ii]
    #print(kk)
    if ii>0:
        return False
    else:
        return True
fin = open ('runround.in', 'r')
fout = open ('runround.out', 'w')

M = int(fin.readline().strip())
r=M+1
#print(isRunround(142))
#print(isRunround(147))
while not isRunround(r):
    r+=1
print(r)
fout.write(str(r)+"\n")
                
fout.close()
    
