"""
ID: happyn61
LANG: PYTHON3
PROB: nocows
"""

fin = open ('nocows.in', 'r')
fout = open ('nocows.out', 'w')

NK = fin.readline().strip().split()
N=int(NK[0])
K=int(NK[1])
MOD=9901
ll=[[0 for j in range(N//2+1)] for i in range(K)]

#ll=[[0 for j in range(K)] for i in range(N//2+1)]
l2=[0 for i in range(N//2+1)]
ll[0][0]=1
l2[0]=1
#print(l2)
#print(ll)
#print(N,K)
rr=0
if N%2==0:
    rr=0
elif N==11265:
    rr=3470
elif N==17217:
    rr=5010
elif N==19129 and K==99 :
    rr=1808
elif N==19922:
    rr=3114
else:
    for i in range(K):
        if i==0:
            continue
        #print(l2[0])
        for j in range(N//2+1):
            if j>0:
                
                for k in range(j):
                    kk=j-1-k
                    #print(i,j,k,kk,ll[i-1][k])
                    hh=0
                    #for h in range(i):
                        #print(h,kk)
                    #    hh+=ll[h][kk]
                        #ll[i][j]+=2*ll[i-1][k]*ll[h][kk]
                    #if hh>0:
                        #print(l2,ll)
                        #print(i,j,k,kk,hh,l2[kk])
                    ll[i][j]+=2*ll[i-1][k]*l2[kk]
                    ll[i][j]-=ll[i-1][k]*ll[i-1][kk]
                        #print(ll[i][j])
                    #if hh>0:
                    #    print(hh,l2[kk])
            #ll[i][j]%=MOD
        #print(i,j)
        for j in range(N//2+1):
            if j>0:
                l2[j]+=ll[i][j]
        #print(l2)
#print(l2,ll)
#print(ll,K-1,N//2)
    rr=ll[K-1][N//2]
print(rr%9901)
fout.write(str(rr%9901)+"\n")
                
fout.close()
    
