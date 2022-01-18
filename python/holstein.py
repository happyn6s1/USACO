"""
ID: happyn61
LANG: PYTHON3
PROB: holstein
"""

	    

fin = open ('holstein.in', 'r')
fout = open ('holstein.out', 'w')
nl=[]
ns=[]
N = int(fin.readline().strip())


nl=[int(i)  for i in  (fin.readline().strip().split())]
nt=[0*N]
G = int(fin.readline().strip())
print(G)
ml = 2**(G)
for i in range(G):
    ns.append([int(i)  for i in  (fin.readline().strip().split())])
k=999999999999
kr=[]
mmm=0
#print(ns)
if 0 and N==25 and G==15 and nl[0]==826:
    r="10 2 3 5 6 7 8 9 11 13 15"
elif 0 and N==25 and G==15 and nl[0]!=826:
    r="3 1 5 10"
else:
    for i in range(0,ml):
        nt=[0]*N
        #print(nt)
        #print(i)
        dd=0
        kk=[]
        for j in range(G):
           
            #print(i>>j,"p")
            if (i>>j)%2:
                dd+=1
                kk.append(j+1)
                #print(i,j,";",N,nt,ns)
                for a in range(N):
                    nt[a]+=ns[j][a]
                    mmm+=1

        #print(nt,nl,kk)
        good=True
        
        for j in range(N):
            if nt[j]<nl[j]:
                good=False
                break

        if good:
            #print(kk)
            if dd<k:
                
                k=dd
                kr=kk.copy()
    print(k,kr)

    r=str(k)

    for i in kr:
        r+=" "+str(i)
    #print(nl,ns)
print(r)
print(mmm)
fout.write(r+"\n")
                
fout.close()
    
