"""
ID: happyn61
LANG: PYTHON3
PROB: cowmbat
"""
import collections
import sys


        
fin = open ('citystate.in', 'r')
fout = open ('citystate.out', 'w')
N=int(fin.readline().strip())


mm=0
#for each mod min and max
#ma = [ [ 0 for i in range(2) ] for j in range(7) ]
#ml= [int(fin.readline().strip()) for j in range(N)]
#ml=[int(i) for i in fin.readline().strip().split()]
#print (ml)
#p= [0 for j in range(N)]
#pst= [0 for j in range(N+1)]

#printdict{}
dd={}
for i in range(N):
    st=fin.readline().strip().split()
        
    if st[1]+st[0][:2] in dd and st[1] != st[0][:2]:
        #dd[st[1]+st[0]]
        mm+=dd[st[1]+st[0][:2]]
        #print(st,st[1]+st[0][:2],dd[st[1]+st[0][:2]])
    if st[0][:2]+st[1] in dd:
        dd[st[0][:2]+st[1]]+=1
        #print(st[0][:2]+st[1])
    else:
        dd[st[0][:2]+st[1]]=1

#print(dd,len(dd))
print(mm)
nn=99999
nnn=-1

'''
    ml=int(fin.readline().strip())
    ss=(ss+ml)%7
    pre[i+1]=ss
    if ma[ss][0]==0:
        ma[ss][0]=i+1
        ma[ss][1]=i+1
    else:
        if (i+1) < ma[ss][0]:
            ma[ss][0]=i+1
        elif ma[ss][1] < (i+1):
            ma[ss][1]=i+1

for i in range(7):
    print(i)
    if ma[i][1]-ma[i][0]>mm:
        mm=ma[i][1]-ma[i][0]
'''

                                   
print(mm)
fout.write (str(mm)+'\n')
fout.close()
