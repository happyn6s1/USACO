"""
ID: happyn61
LANG: PYTHON3
PROB: haircut
"""
def getsum(BITTree,i): 
    s = 0 #initialize result 
  
    # index in BITree[] is 1 more than the index in arr[] 
    i = i+1
  
    # Traverse ancestors of BITree[index] 
    while i > 0: 
  
        # Add current element of BITree to sum 
        s += BITTree[i] 
  
        # Move index to parent node in getSum View 
        i -= i & (-i) 
    return s 
  
# Updates a node in Binary Index Tree (BITree) at given index 
# in BITree. The given value 'val' is added to BITree[i] and 
# all of its ancestors in tree. 
def updatebit(BITTree , n , i ,v): 
  
    # index in BITree[] is 1 more than the index in arr[] 
    i += 1
  
    # Traverse all ancestors and add 'val' 
    while i <= n: 
  
        # Add 'val' to current node of BI Tree 
        BITTree[i] += v 
  
        # Update index to that of parent in update View 
        i += i & (-i) 
  
  
# Constructs and returns a Binary Indexed Tree for given 
# array of size n. 
def construct(arr, n): 
  
    # Create and initialize BITree[] as 0 
    BITTree = [0]*(n+1) 
  
    # Store the actual values in BITree[] using update() 
    for i in range(n): 
        updatebit(BITTree, n, i, arr[i]) 
  
    # Uncomment below lines to see contents of BITree[] 
    #for i in range(1,n+1): 
    #     print BITTree[i], 
    return BITTree 
	    

fin = open ('haircut.in', 'r')
fout = open ('haircut.out', 'w')
from datetime import datetime
#print(datetime.now())
N = int(fin.readline().strip())
ol= list(map(int,fin.readline().strip().split()))
suml=[]
#od={i:[] for i in range(max(ol)+1)}
d={i:[] for i in set(ol)}
sl=[k for k in d]
sl.sort(reverse=True)
dd={}
i=0
for i in range(len(sl)):
    dd[sl[i]]=i
    
#print(sl,dd)
#print(od,d,ol)
from datetime import datetime
#print(datetime.now())
for i in range(len(ol)):
    d[ol[i]].append(i)
#print(od,d,ol)
freq=[0 for i in range(len(d))]
BITTree=construct(freq,len(freq))
print(datetime.now())
for i in ol:
    freq[dd[i]]+=1
    updatebit(BITTree, len(freq), dd[i], 1)
    if dd[i]==0:
        suml.append(0)
    else:
        suml.append(getsum(BITTree,dd[i]-1))

#print(suml)

nl=[ 1 for i in range(N)] #
s=0
#print(ol,d,nl)
#print(s)
fout.write(str(s)+"\n")
from datetime import datetime
print(datetime.now())
for i in range(1,N):
    
    #print(s)
    if i-1 in d:
        for j in d[i-1]:
            
            s+=suml[j]
    
    #print(nl)
    #print(s)
    #ns.append(s)
    fout.write(str(s)+"\n")
from datetime import datetime
print(datetime.now())    
#ns.reverse()
#print(ns)
    
                
fout.close()
    
