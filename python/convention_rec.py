"""
ID: happyn61
LANG: PYTHON3
PROB: friday
"""

outcome=[]
def maxtime(arrivetimes,buses,limit):
    if arrivetimes ==[]:
        return 0
    if len(arrivetimes)==buses*limit:
        max=0
        for i in range(buses):
            #print(arrivetimes,limit*i)
            localmax=  arrivetimes[limit*(i+1)-1]-arrivetimes[i*limit]
            #print(localmax)
            if localmax > max:
                max = localmax
        #print(max)
        return max
    else:
        min=10**6
        max=0
        for i in range(1,limit+1):
            if i > len(arrivetimes):
                continue
            copy=arrivetimes.copy()
            max=arrivetimes[-1]-arrivetimes[-i]
            print(i,copy,copy[0:-i],buses,max)
            
            m=maxtime(copy[0:-i],buses-1,limit)
            if m>max:
                max=m
            if max < min:
                min=max
        return min
        #print("2"+str(min))

#print(maxtime([1,3,4,9,14],3,2))
fin = open ('convention.in', 'r')
fout = open ('convention.out', 'w')

m,n,c=map(int,fin.readline().strip().split())
arr=list(map(int,fin.readline().strip().split()))
arr.sort()

#print(len(set(outcome)))
fout.write (str(maxtime(arr,n,c))+'\n')
#fout.write (str(y[1])+'\n')
#fout.write (str(y[2])+'\n')
#    print(names[i] + ' '+str(money[i])+'\n')
    
fout.close()
