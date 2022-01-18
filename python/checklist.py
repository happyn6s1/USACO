"""
ID: happyn61
LANG: PYTHON3
PROB: checklist
"""

def findandinsert(ll,lr,m,k):
    if len(ll)==0:
        ll.append(m)
        return
    
    lo=0
    hi=len(ll)
    ist=0
    if m<ll[0]:
        ll.insert(0,m)
        ist=0
    elif m>ll[-1]:
        ll.append(m)
        ist=len(ll)-1
    else:
        while lo<hi-1:
            mi=(hi+lo)//2
            if m>ll[mi]:
                lo=mi
            else:
                hi=mi
            
        ll.insert(hi,m)
        ist=hi
    #print(ll,ist)
    if  ((len(ll)-ist-1)>2*ist or ist > 2*(len(ll)-ist-1)):
        lr.append(k)
        print(k)
def d(c1,c2):
    #print(c1,c2)
    return (c1[0]-c2[0])**2+(c1[1]-c2[1])**2
fin = open ('checklist.in', 'r')
fout = open ('checklist.out', 'w')

#cowlist=[]

h,g=list(map(int,fin.readline().strip().split()))
#print(h,g)
mmm=99999999999
dp=[[[mmm,mmm] for j in range (g+1)]  for i in range(h+1)] #means i*H and j*G, minimum of cost, end with H(0) or G(0)
hl=[[0,0]]
gl=[[0,0]]
for i in range(h):
    hl.append(list(map(int,fin.readline().strip().split())))
for i in range(g):
    gl.append(list(map(int,fin.readline().strip().split())))
#print(hl,"\n",gl)
#d[H][G]


#dh, dg    
#print(l)
smax=0
dp[1][0][0]=0
dg=[0]
for j in range(1,g+1):
    dg.append(d(gl[j-1],gl[j]))
for i in range(1,h):
    dh=d(hl[i-1],hl[i])
    for j in range(g+1):
        
        if i==1:
            if j>0:
                #print(min(d(hl[i],gl[j]),d(gl[j-1],gl[j])))
                dp[i][j][1]=min(dp[i][j-1][0]+d(hl[i],gl[j]),dp[i][j-1][1]+dg[j])
                #print(dp[i])
        
            
        else:
            if j==0:
                #print(i,dp[i-1][j][0],d(hl[i-1],hl[i]))
                dp[i][j][0]=dp[i-1][j][0]+dh
                
            else:
                dd=d(gl[j],hl[i])
                #print (d(hl[i-1],hl[i]),d(hl[i-1],hl[i])+dp[i][j-1][0])
                dp[i][j][0]=min(dp[i-1][j][0]+dh,dp[i-1][j][1]+dd)
                
                dp[i][j][1]=min(dp[i][j-1][1]+dg[j],dp[i][j-1][0]+dd)
                
                #print(i,j,dp[i][j])
#print(dp)
#print(min(dp[-2][-1][0]+d(hl[-2],hl[-1]),dp[-2][-1][1]+d(gl[-1],hl[-1])))

smax=min(dp[-2][-1][0]+d(hl[-2],hl[-1]),dp[-2][-1][1]+d(gl[-1],hl[-1]))
#print(len(rl),rl)
print(smax)
fout.write (str(smax)+'\n')
#fout.write (str(y[1])+'\n')
#fout.write (str(y[2])+'\n')
#    print(names[i] + ' '+str(money[i])+'\n')
    
fout.close()
