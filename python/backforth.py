"""
ID: happyn61
LANG: PYTHON3
PROB: friday
"""

outcome=[]
def movebucket(startwith,daysleft,bucketslist,outcome):
    src=startwith%2
    tgt=(startwith+1)%2
    if daysleft==0:
        srcset=set(bucketlist[src])
        for i in srcset:
            for j in range(len(outcome)):
                outcome[j]+=i
        
        

fin = open ('backforth.in', 'r')
fout = open ('backforth.out', 'w')

twobuckets=[]

for i in range(2):
    bucket=list(map(int,fin.readline().strip().split()))
    twobuckets.append(bucket)

print(twobuckets)

for i in set(twobuckets[0]):
    for j in set(twobuckets[1]):
        bucket0=twobuckets[0].copy()
        bucket1=twobuckets[1].copy()
        bucket0.remove(i)
        bucket0.append(j)
        bucket1.remove(j)
        bucket1.append(i)
        outcome.append(j-i)
        
        for k in set(bucket0):
            for l in set(bucket1):
                 outcome.append(j-i+l-k)
                 
print(len(set(outcome)))
fout.write (str(len(set(outcome)))+'\n')
#fout.write (str(y[1])+'\n')
#fout.write (str(y[2])+'\n')
#    print(names[i] + ' '+str(money[i])+'\n')
    
fout.close()
