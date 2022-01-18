class Solution:
    def findMinFibonacciNumbers(k: int) -> int:
        
        m=1000000000+2
        dp=[0 for i in range(k+1)]
        dp[0]=0
        dp[1]=1
        f=[0,1,1]
        i=3
        while True:
            if (f[i-1]+f[i-2])>(k):
                break
            f.append(f[i-1]+f[i-2])
            #print(f)
            dp[f[-1]]=1
            i+=1
        #ff=set(f)
        last=0
        for i in range(1,k+1):
            if dp[i]==1:
                last=i
            else:
                dp[i]=dp[i-last]+dp[last]
            '''
            lo=f[0]
            hi=len(f)-1
            j=f[0]
            while lo<=hi:
                
                mi=(lo+hi)//2
                #print(i,lo,hi,mi)
                if f[mi]==i:
                    #print("aa",i)
                    j=f[mi]
                    break
                elif f[mi]>i:
                    hi=mi-1
                else:
                    j=max(j,f[mi])
                    lo=mi+1
                    
                
            if i==j:
                dp[i]=1
            else:
                #print(i,j)
                dp[i]=dp[j]+dp[i-j]
            #print(i,j,dp)
            '''
            
        #print(dp) 
        #print(max(dp))
        return dp[k]
print(Solution.findMinFibonacciNumbers(3719468))
