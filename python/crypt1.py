"""
ID: happyn61
LANG: PYTHON3
PROB: crypt1
"""

#from collections import defaultdict

#import heapq

fin = open ('crypt1.in', 'r')
fout = open ('crypt1.out', 'w')
#print(dic["4734"])
N=int(fin.readline().strip())


nl=[]
nd=[]
#nl=[[0,-1] for i in range(N)]
ss=0

nl=set(int(i) for i in fin.readline().strip().split())
print(nl)
mm=0 
for a in range(1,10):
    for b in range(10):
        for c in range(10):
            for d in range(1,10):
                if (100*a+10*b+c)*d>=1000:
                        continue
                for e in range(10):
                    if (100*a+10*b+c)*e>=1000:
                        continue
                    if (100*a+10*b+c)*(10*d+e)>=10000:
                        continue
                    k=(100*a+10*b+c)*e
                    q=(100*a+10*b+c)*d
                    p=(100*a+10*b+c)*(10*d+e)
                    ss=set()
                    ss.add(a)
                    ss.add(b)
                    ss.add(c)
                    ss.add(e)
                    ss.add(d)
                    for j in (k,p,q):
                        for i in range(4):
                            if i==3 and j!=p:
                                break
                            ss.add((j//(10**i))%10)


                    #print(ss)

                    if ss.issubset(nl):
                        mm+=1
                        #print(a,b,c,d,e)
                

print(mm)
nd.sort(reverse=True)
tt=0
print(nl,nd)
   
  

fout.write (str(mm)+'\n')
fout.close()
