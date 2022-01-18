"""
ID: happyn61
LANG: PYTHON3
PROB: milk3
"""

#from collections import defaultdict

#import heapq

fin = open ('milk3.in', 'r')
fout = open ('milk3.out', 'w')
#print(dic["4734"])
ABC=(fin.readline().strip().split())
A=int(ABC[0])
B=int(ABC[1])
C=int(ABC[2])
a=0
b=0
c=C

mm=0

setq=set()
setq.add((a,b,c))
setr=set()
nl=[]
nd=[]
#nl=[[0,-1] for i in range(N)]
ss=0
t=setq.pop()
while t :
    setr.add(t)
    #print(t)
    if t[0]>0:
        if t[1]<B :
            #print(t)
            if t[0]>(B-t[1]):
                if (t[0]+t[1]-B,B,t[2]) not in setr:
                    setq.add((t[0]+t[1]-B,B,t[2]))
            else:
                if (0,t[0]+t[1],t[2]) not in setr:
                    setq.add((0,t[0]+t[1],t[2]))
        if t[2]<C:
            if t[0]>(C-t[2]):
                if (t[0]+t[2]-C,t[1],C) not in setr:
                    setq.add((t[0]+t[2]-C,t[1],C))
            else:
                if (0,t[1],t[0]+t[2]) not in setr:
                    setq.add((0,t[1],t[0]+t[2]))
    if t[1]>0:
        if t[0]<A :
            #print(t,A,B,C,"qqqq")
            if t[1]>(A-t[0]):
                if (A,t[0]+t[1]-A,t[2]) not in setr:
                    setq.add((t[0]+t[1]-A,A,t[2]))
            else:
                if (t[0]+t[1],0,t[2]) not in setr:
                    setq.add((0,t[0]+t[1],t[2]))
        if t[2]<C:
            
            if t[1]>(C-t[2]):
                if (t[0],t[1]+t[2]-C,C) not in setr:
                    setq.add((t[0],t[1]+t[2]-C,C))
            else:
                if (t[0],0,t[1]+t[2]) not in setr:
                    setq.add((t[0],0,t[1]+t[2]))
    if t[2]>0:
        #print(t,A,B,C,"qq")
        if t[0]<A :
            if t[2]>(A-t[0]):
                if (A,t[1],t[2]+t[0]-A) not in setr:
                    #print(A,t[1],t[2]+t[0]-A)
                    setq.add((A,t[1],t[2]+t[0]-A))
            else:
                if (t[0]+t[2],t[1],0) not in setr:
                    setq.add((t[0]+t[2],t[1],0))
        if t[1]<B:
            #print(t)
            if t[2]>(B-t[1]):
                #print(t[0],B,t[1]+t[0]-B)
                if (t[0],B,t[1]+t[2]-B) not in setr:
                    setq.add((t[0],B,t[1]+t[2]-B))
            else:
                if (t[0],t[1]+t[2],0) not in setr:
                    setq.add((t[0],t[1]+t[2],0))
    #print(setr)
    #print(setq,"q")
    if len(setq)>0:
        t=setq.pop()
    else:
        t=None
    #print(t)
#nl=[int(i) for i in fin.readline().strip().split()]
#ml=[int(i) for i in fin.readline().strip().split()]

#print(setr)

for i in setr:
    if i[0]==0 :
        if i[2] not in nl:
            nl.append(i[2])
nl.sort()
mm=""
for i in nl:
    mm+=str(i)+" "

    
print(mm.strip())
ml=[1, 0, 3, 2]
fout.write (str(mm.strip())+'\n')
fout.close()
