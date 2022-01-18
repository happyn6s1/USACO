"""
ID: happyn61
LANG: PYTHON3
PROB: hps
"""

	    

fin = open ('hps.in', 'r')
fout = open ('hps.out', 'w')
[N,K]= list(map(int,fin.readline().strip().split()))
l=[]
for i in range(N):
    l.append(fin.readline().strip())
s="HPS"
d={"H":0,"P":1,"S":2}
o={"H":"PS","S":"PH","P":"HS"}
dp=[[[0,0,0] for j in range(N)] for i in range(K+1)]
#H P S , 0 , 1 , 2


for i in range(K+1):
    for j in range(N):
        if i==0:
                
            if j>0:
                dp[i][j][0]=dp[i][j-1][0]
                dp[i][j][1]=dp[i][j-1][1]
                dp[i][j][2]=dp[i][j-1][2]
                dp[i][j][d[l[j]]]+=1
                #dp[i][j]=dp[i][j-1]
            else:
                dp[i][j][d[l[j]]]=1
                
        else:
            if j>0:
                for k in range(3):
                    #t=[0,0,0]
                    #t[d[l[j]]]=1
                    t=1 if l[j]==s[k] else 0
                    #print(dp,i,j,k)
                    #dp[i][j][k]=max(dp[i][j-1][k]+t[k],max(dp[i-1][j-1][(k+1)%3]+t[(k+1)%3],dp[i-1][j-1][(k+2)%3]+t[(k+2)%3]))
                    dp[i][j][k]=max(dp[i][j-1][k],max(dp[i-1][j-1][(k+1)%3],dp[i-1][j-1][(k+2)%3]))+t
            else:
                dp[i][j][d[l[j]]]=1

#print(dp)                
fout.write(str(max(dp[-1][-1]))+"\n")
#print(dp[-1][-1])
'''for ii in range(N):
    i=ii+1
    #print(i)
    if dp[i]==i or dp[i]==-1:
        s+=1
print(s)
'''    
#ns.reverse()
#print(ns)
    
                
fout.close()
    
