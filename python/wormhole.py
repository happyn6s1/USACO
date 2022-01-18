"""
ID: happyn61
LANG: PYTHON3
PROB: wormhole
"""

#from collections import defaultdict

#import heapq
def permutation(lst): 
  
    # If lst is empty then there are no permutations 
    if len(lst) == 0: 
        return [] 
  
    # If there is only one element in lst then, only 
    # one permuatation is possible 
    if len(lst) == 1: 
        return [lst] 
  
    # Find the permutations for lst if there are 
    # more than 1 characters 
  
    l = [] # empty list that will store current permutation 
  
    # Iterate the input(lst) and calculate the permutation 
    for i in range(len(lst)): 
       m = lst[i] 
  
       # Extract lst[i] or m from the list.  remLst is 
       # remaining list 
       remLst = lst[:i] + lst[i+1:] 
  
       # Generating all permutations where m is first 
       # element 
       for p in permutation(remLst): 
           l.append([m] + p) 
    return l

def perm2(lst): 
  
    # If lst is empty then there are no permutations 
    if len(lst) == 0: 
        return [] 
  
    # If there is only one element in lst then, only 
    # one permuatation is possible 
    if len(lst) == 2: 
        return [lst] 
  
    # Find the permutations for lst if there are 
    # more than 1 characters 
  
    l = [] # empty list that will store current permutation 
  
    # Iterate the input(lst) and calculate the permutation 
    for i in range(1):
        for j in range(i+1,len(lst)):
            m = lst[i] 
            n = lst[j]
            
           # Extract lst[i] or m from the list.  remLst is 
           # remaining list 
            remLst = lst[:i] + lst[i+1:j]+lst[j+1:] 
            #print(remLst)
           # Generating all permutations where m is first 
           # element 
            for p in perm2(remLst): 
                l.append([m] +[n] + p) 
    return l  
fin = open ('wormhole.in', 'r')
fout = open ('wormhole.out', 'w')
#print(dic["4734"])
N=int(fin.readline().strip())
mm=0
def hasnext(nl,i):
    mi=-9999999999
    m=None
    for j in range(len(nl)):
        
        if j==i:
            continue
        #print(i,j,nl[j],nl[i],m,mi)
        if nl[j][1]==nl[i][1] and nl[j][0] > nl[i][0]:
            if m == None:
                mi=nl[j][0]
                m=j
                #print("m",m)
            else:
                if nl[j][0]<mi:
                    mi=nl[j][0]
                    m=j
                    #print("mm",m)
    return m
def check(ml,nl):
    res=True
    for i in range(len(nl)):
        sss=set()
        #sss.add(i)
        #print(i,sss)
        j=i
        while True:
        
            nnext=hasnext(nl,j)
            if nnext == None:
                break
            #print(j,"nnext",nnext)
            if nnext in sss:
                #print("ijn",i,j,nnext)
                return False
            sss.add(nnext)
            j=ml[nnext]
            #print("jj",j)
            #if j in sss:
            #    return False
                #print("ijm",i,j,nnext)
            #sss.add(j)
            #print(sss,"sss")

    return res

nl=[]
nd=[]
#nl=[[0,-1] for i in range(N)]
ss=0

#nl=[int(i) for i in fin.readline().strip().split()]
#ml=[int(i) for i in fin.readline().strip().split()]

for i in range(N):
    ll=[int(j) for j in fin.readline().strip().split()]
    ll.append(0)
    nl.append(ll)

pl=perm2([int(i) for i in range(N)])
ml=[0 for i in range(N)]
#print(pl)
#print(hasnext(nl,5),"555")
for i in range(len(pl)):
    for j in range(N//2):
        ml[pl[i][j*2]]=pl[i][j*2+1]
        ml[pl[i][j*2+1]]=pl[i][j*2]
    #print(ml)
    if not check(ml,nl):
        print(ml,"p")
        mm+=1
#print(nl)
#print(ml)
print(mm)
ml=[1, 0, 3, 2]
#print(check(ml,nl),"ok")
fout.write (str(mm)+'\n')
fout.close()
