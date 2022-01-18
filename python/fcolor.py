"""
ID: happyn61
LANG: PYTHON3
PROB: fcolor
"""

	    

fin = open ('fcolor.in', 'r')
fout = open ('fcolor.out', 'w')
df={}
def fp(i):
    #print(i)
    if dp[i]==i:
        return i
    else:
        return fp(dp[i])
def merge(i,j):
    print("merge",i,j)
    if i==-1 and j==-1:
        return
    if i==j:
        return
    
    if fp(i)!=fp(j):
        M=False
        if dc[fp(i)]!=-1 and dc[fp(j)]!=-1:
            M=True
            x=dc[fp(i)]
            y=dc[fp(j)]
        #print(fp(i),fp(j),dc[fp(i)],dc[fp(j)],"qwerqwe")
        if fp(i)>fp(j):
            if dc[fp(i)]>0:
                dc[fp(j)]=dc[fp(i)]
            dp[fp(i)]=fp(j)
            
        else:
            if dc[fp(j)]>0:
                dc[fp(i)]=dc[fp(j)]
            dp[fp(j)]=fp(i)
        if M:
            merge(x,y)
        #print(dc,dp)
        #print(dc[i],dc[j])            
    #print(dp,"end")
def find(parent, i): 
	if parent[i] == i: 
		return i 
	return find(parent, parent[i]) 

# A function that does union of two sets of x and y 
# (uses union by rank) 
def union(parent, rank, x, y): 
	xroot = find(parent, x) 
	yroot = find(parent, y) 

	# Attach smaller rank tree under root of  
	# high rank tree (Union by Rank) 
	if rank[xroot] < rank[yroot]: 
		parent[xroot] = yroot 
	elif rank[xroot] > rank[yroot]: 
		parent[yroot] = xroot 

	# If ranks are same, then make one as root  
	# and increment its rank by one 
	else : 
		parent[yroot] = xroot 
		rank[xroot] += 1
# The main function that prints the Minimum  
# Spanning Tree(MST) using the Prim's Algorithm.  
# It is a O(ELogV) function


[N,M]= list(map(int,fin.readline().strip().split()))
#ol= list(map(int,fin.readline().strip().split()))
graph=[[]for i in range(N+1)]
dp=[i for i in range(N+1)] #means parent()
rank=[0 for i in range(N+1)]
stack=[]
for i in range(M):
    a,b= list(map(int,fin.readline().strip().split()))
    if graph[a]!=[] and find(dp,graph[a][0])!=find(dp,b):
        stack.append((graph[a][0],b))
    graph[a].append(b)
print(len(stack))    
while stack:
    c,d=stack.pop()
    if find(dp,c)!=find(dp,d):
        union(dp,rank,c,d)
        if len(graph[c])>0 and len(graph[d])>0:
            stack.append((graph[c][0],graph[d][0]))

#print(dp)        
        
s=1
#print(dp)
dd={}
for i in range(N):
    if find(dp,i+1) not in dd:
        dd[find(dp,i+1)]=s
        s+=1
    #print(i+1,dd[find(dp,i+1)],find(dp,i+1))
    fout.write(str(dd[find(dp,i+1)])+"\n")
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
    
