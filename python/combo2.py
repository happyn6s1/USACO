"""
ID: happyn61
LANG: PYTHON3
PROB: combo
"""

#from collections import defaultdict

#import heapq

fin = open ('combo.in', 'r')
fout = open ('combo.out', 'w')
#print(dic["4734"])
N=int(fin.readline().strip())


nl=[]
nd=[]
#nl=[[0,-1] for i in range(N)]
ss=0

nl=[int(i) for i in fin.readline().strip().split()]
ml=[int(i) for i in fin.readline().strip().split()]


if N>=10:
    nn=1

    for i in range(3):
        k=abs(nl[i]-ml[i])
        #print(N,i,k,nn)
        if k<=4:
            nn*=(5-k)
        elif k>=(N-5+1):
            nn*=(k-N+5)
        else:
            nn=0
    mm=250-nn
else:
    mm=0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                #print(i,j,k)
                if ((abs(i-nl[0])<=2 or abs(i-nl[0])>=(N-2)) and \
                    (abs(j-nl[1])<=2 or abs(j-nl[0])>=(N-2)) and \
                    (abs(k-nl[2])<=2 or abs(k-nl[0])>=(N-2)) 
                    or 
                    (abs(i-ml[0])<=2 or abs(i-ml[0])>=(N-2)) and \
                    (abs(j-ml[1])<=2 or abs(j-ml[0])>=(N-2)) and \
                    (abs(k-ml[2])<=2 or abs(k-ml[0])>=(N-2)) ):
                    #print("good",i,j,k)
                    mm+=1
print(mm)
fout.write (str(mm)+'\n')
fout.close()
