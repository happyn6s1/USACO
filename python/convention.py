"""
ID: happyn61
LANG: PYTHON3
PROB: friday
"""

fin = open ('convention.in', 'r')
fout = open ('convention.out', 'w')

m,n,c=map(int,fin.readline().strip().split())
arr=list(map(int,fin.readline().strip().split()))
arr.sort()
limit=c
s=[[0,0,0,0,0,0,0,0]]

for bus in range(1,n+1):
    lb=limit*bus
    lb1=lb-limit
    ss=[]
    if bus == 1:
        for i in range(lb):
            ss.append(arr[i]-arr[0])
            #print(arr[i]-arr[0],arr)
    else:        
        for i in range(lb):
            if i >= m:
                continue
            if i<bus:
                ss.append(0)
                continue
            #print(arr,i,bus,s)
                            
            mi=max(arr[i]-arr[i+1-limit],s[bus-1][i-limit])
                    
            for j in range(1,limit+1):
                    #print(bus,limit,i,j)
                    if i-j<lb1:
                        mm=max(arr[i]-arr[i+1-j],s[bus-1][i-j])
                        if   mm<mi :
                            mi =mm
            #print(ss,bus,i)
            ss.append(mi)
    #print(ss)
    s.append(ss)
#print(s)                     
#print(len(set(outcome)))
print(s)
fout.write (str(s[n][m-1])+'\n')
#fout.write (str(y[1])+'\n')
#fout.write (str(y[2])+'\n')
#    print(names[i] + ' '+str(money[i])+'\n')
    
fout.close()
