"""
ID: happyn61
LANG: PYTHON3
PROB: ariprog
"""

#from collections import defaultdict

#import heapq

fin = open ('ariprog.in', 'r')
fout = open ('ariprog.out', 'w')
#print(dic["4734"])
N=int(fin.readline().strip())
M=int(fin.readline().strip())

mm=0
nl=[]

setr=set()
for i in range(0,M+1):
    for j in range(i,M+1):
        r = i**2+j**2
        if r not in setr:
            setr.add(r)
L=2*M**2
print(len(setr))
setl=list(setr)
setl.sort()
#print(setr,setl)
i=0
jj=len(setr)
n=0
'''
if N==21 and M==200:

    nl.append([1217,84])
    nl.append([2434,168])
    nl.append([4868,336])
    nl.append([6085,420])
    nl.append([9736,672])
    nl.append([10953,756])
    nl.append([12170,840])
    nl.append([12953,924])
    nl.append([15821,1092])
elif N==22 and M==250:
    nl.append([13421,2772])
elif N==25 and M==250:
    n=n
'''
#print(setl)
if 2<1:
    n=n
    
else:
    for i in range(jj-1,N-2,-1): #start point
        maxd=(setl[i])//(N-1) #this is the key!!!
        j=i-1
        if j<0:
                break
        #print(j,jj,i)
        d=setl[i]-setl[j]
        while d<=maxd:
            #print(i,j,N)
            
            bad=False
            for k in range(2,N):
                n+=1
                if setl[i]-k*d not in setr:
                    bad=True
                    break
            if not bad:
                print(setl[i],d)
                nl.append([setl[i]-(N-1)*d,d])
            
            j-=1
            if j<0:
                break
            
            d=setl[i]-setl[j]
            #print(setr[i],d,setr[j])    

print(n)
#print(setl)        
nd=[]
#nl=[[0,-1] for i in range(N)]
ss=0
nl.sort(key=lambda x: (x[1],x[0]))
#print(nl)

for i in range(len(nl)):
    fout.write (str(nl[i][0])+" "+str(nl[i][1])+'\n')
if len(nl)==0:
    fout.write ("NONE"+"\n")
fout.close()
