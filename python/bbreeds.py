"""
ID: happyn61
LANG: PYTHON3
PROB: sort
"""

    
fin = open ('bbreeds.in', 'r')
fout = open ('bbreeds.out', 'w')
#print(dic["4734"])
bl=list(fin.readline().strip())
N=len(bl)
sl=[[0 for x in range(N)] for y in range(N//2+1)]
#print(bl,N)
rn=0
for i in range(N):
    if bl[i]=='(':
        rn+=1
    else:
        rn-=1
    for j in range(N//2+1):
        if i==0:
            
            if j < 2:
                sl[j][i]=1
            else:
                sl[j][i]=0
            continue    
        if bl[i]=='(':
            
            if j > 0 :
                sl[j][i]=sl[j][i-1]+sl[j-1][i-1]
            else:
                sl[j][i]=sl[j][i-1]
        else:
            
            #print(rn,j)
            if rn >= j:
                if j < N//2:
                    sl[j][i]=sl[j][i-1]+sl[j+1][i-1]
                else:
                    sl[j][i]=sl[j][i-1]
            else:
                if j < N//2:
                    sl[j][i]=sl[j+1][i-1]
        
            

print(sl[0][N-1]%2012)
print(sl)
#    print(names[i] + ' '+str(money[i])+'\n')
fout.write (str(sl[0][N-1]%2012)+'\n')  
fout.close()
