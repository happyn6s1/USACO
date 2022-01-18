"""
ID: happyn61
LANG: PYTHON3
PROB: lamps
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
fin = open ('lamps.in', 'r')
fout = open ('lamps.out', 'w')

N = int(fin.readline().strip())
C = int(fin.readline().strip())
ON= list(map(int,fin.readline().strip().split()))
s1=set()
n1=0
n2=0
for i in range(len(ON)-1):
    ON[i]=ON[i]-1
    if ON[i]%6 not in s1:
        s1.add(ON[i]%6)
        print
        n1+=2**(5-ON[i]%6)
print(n1)
OFF= list(map(int,fin.readline().strip().split()))
s2=set()
for i in range(len(OFF)-1):
    OFF[i]=OFF[i]-1
    if OFF[i]%6 not in s2:
        s2.add(OFF[i]%6)
        n2+=2**(5-OFF[i]%6)

#print(ON,OFF,s1,s2,n1,n2,C)
s=set()
ss=set()
ss.add(0)
s.add(0)
ls=[]
#C=1
print(C)
s0=set()
s0.add(63)
ls.append(s0)
for i in range(1,20):
    aaa=ls[i-1]
    #print(aaa)
    aa=aaa.copy()
    s0=set()
    while aa:
        a=aa.pop()
        b=a^63
        s0.add(b)
        b=a^21
        s0.add(b)
        b=a^42
        s0.add(b)
        b=a^36
        s0.add(b)
    ls.append(s0)
#print(ls)
notp=True
if s1.intersection(s2):
    notp=True
    #print(s1,s2)
else:
    if C==1:
        for i in (0, 21,27, 42):
            #print(n1,n2,i,(63-n1) | i,n2 & i)
            if (63-n1) | i ==63 and n2 & i ==0:
                print(i)
                str1=""
                for k in range(N):
                    if 2**(5-(k)%6) & i:
                        str1+="1"
                    else:
                        str1+="0"
                print(str1)
                fout.write(str1+"\n")
                notp=False
    elif C==0:
        for i in [63]:
            #print(n1,n2,i,(63-n1) | i,n2 & i)
            if (63-n1) | i ==63 and n2 & i ==0:
                print(i)
                str1=""
                for k in range(N):
                    if 2**(5-(k)%6) & i:
                        str1+="1"
                    else:
                        str1+="0"
                print(str1)
                fout.write(str1+"\n")
                notp=False
    elif C==1:
        for i in (0, 14, 21, 36, 42, 49, 63):
            print(n1,n2,i,(63-n1) | i,n2 & i)
            if (63-n1) | i ==63 and n2 & i ==0:
                print(i)
                str1=""
                for k in range(N):
                    if 2**(5-(k)%6) & i:
                        str1+="1"
                    else:
                        str1+="0"
                print(str1)
                fout.write(str1+"\n")
                notp=False
    else:
        for i in (0, 14, 21,27, 36, 42, 49, 63):
            print(n1,n2,i,(63-n1) | i,n2 & i)
            if (63-n1) | i ==63 and n2 & i ==0:
                print(i)
                str1=""
                for k in range(N):
                    if 2**(5-(k)%6) & i:
                        str1+="1"
                    else:
                        str1+="0"
                print(str1)
                fout.write(str1+"\n")
                notp=False
        


#print(ls)
if notp:                
    fout.write("IMPOSSIBLE"+"\n")
r=N+1
#print(r)
#fout.write(str(r)+"\n")
                
fout.close()
    
