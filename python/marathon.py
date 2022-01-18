"""
ID: happyn61
LANG: PYTHON3
PROB: marathon
"""

  
# Driver program to test the above functions 
fin = open ('marathon.in', 'r')
fout = open ('marathon.out', 'w')

from datetime import datetime
print(datetime.now())
N=int(fin.readline().strip())
A=[0]
B=[0]
C=[]
d={0:0}
p=[]
dp=[[0 for i in range(N)] for j in range(2)]
for i in range(N):
    x,y=list(map(int,fin.readline().strip().split()))
    p.append((x,y))
    if i==0:
        continue
    
    if i==N-1 or i==1:
        dp[0][i]=dp[0][i-1]+abs(p[i][0]-p[i-1][0])+abs(p[i][1]-p[i-1][1])
    
        dp[1][i]=dp[1][i-1]+abs(p[i][0]-p[i-1][0])+abs(p[i][1]-p[i-1][1])
    else:
        dp[0][i]=dp[0][i-1]+abs(p[i][0]-p[i-1][0])+abs(p[i][1]-p[i-1][1])
    
        dp[1][i]=min(dp[1][i-1]+abs(p[i][0]-p[i-1][0])+abs(p[i][1]-p[i-1][1]), dp[0][i-2]+abs(p[i][0]-p[i-2][0])+abs(p[i][1]-p[i-2][1]))

print(dp)
fout.write (str(dp[-1][-1])+'\n')
#fout.write (str(y[1])+'\n')
#fout.write (str(y[2])+'\n')
#    print(names[i] + ' '+str(money[i])+'\n')
    
fout.close()
