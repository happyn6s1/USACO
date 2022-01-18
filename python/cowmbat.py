"""
ID: happyn61
LANG: PYTHON3
PROB: cowmbat
"""
import collections
import sys
def traverse(node,vlist):
    #print(root)
    #print(trees[root])
    for c in vlist[node]:
        #print(c)
        nn=vls[node]
        #print(nn)
        vls[c]=vls[c].union(vls[node])
        traverse(c,vlist)

        
fin = open ('cowmbat.in', 'r')
fout = open ('cowmbat.out', 'w')
NM=fin.readline().strip().split()
N=int(NM[0])
M=int(NM[1])
K=int(NM[2])

def floydWarshall(graph,V): 
  
    """ dist[][] will be the output matrix that will finally 
        have the shortest distances between every pair of vertices """
    """ initializing the solution matrix same as input graph matrix 
    OR we can say that the initial values of shortest distances 
    are based on shortest paths considering no  
    intermediate vertices """
    #dist = map(lambda i : map(lambda j : j , i) , graph)
    #dist = [row[:] for row in graph]
    dist=graph
    #print(dist)
    """ Add all vertices one by one to the set of intermediate 
     vertices. 
     ---> Before start of an iteration, we have shortest distances 
     between all pairs of vertices such that the shortest 
     distances consider only the vertices in the set  
    {0, 1, 2, .. k-1} as intermediate vertices. 
      ----> After the end of a iteration, vertex no. k is 
     added to the set of intermediate vertices and the  
    set becomes {0, 1, 2, .. k} 
    """
    for k in range(V): 
  
        # pick all vertices as source one by one 
        for i in range(V): 
  
            # Pick all vertices as destination for the 
            # above picked source 
            for j in range(V): 
  
                # If vertex k is on the shortest path from  
                # i to j, then update the value of dist[i][j] 
                dist[i][j] = min(dist[i][j] , 
                                  dist[i][k]+ dist[k][j] 
                                )
    return dist

def printSolution(dist): 
    print ("Following matrix shows the shortest distances between every pair of vertices" )
    for i in range(V): 
        for j in range(V): 
            if(dist[i][j] == INF): 
                print ("%7s" %("INF"))
            else: 
                print ("%7d\t" %(dist[i][j]))
            if j == V-1: 
                print ("")
if K<=1:
    mm=0
    fout.write (str(mm)+'\n')
    fout.close()
    sys.exit()


keys=list(fin.readline().strip())
for i in range(N):
    keys[i]=ord(keys[i])-ord('a')
                
#print(keys)
matrix = [ [ 999999999 for i in range(M) ] for j in range(N+1) ]
for i in range(M):
    matrix[0][i]=0
tt= [ 0 for i in range(N+1)]
#print(matrix)
root=0
vlist=[]
vls=[]
gg=[]
for i in range(M):
    kk=[int(i) for i in fin.readline().strip().split()]
    gg.append(kk)
    
#print(gg)
floydWarshall(gg,M)
#print(gg)


mm=0
for i in range(K,N+1):
    for j in range(M):
#        print(keys[i-1])
        
        cost1=gg[keys[i-1]][j]+matrix[i-1][j]
        cc=0
        for ii in range(K):
            cc+=gg[keys[i-ii-1]][j]
        
        cost2=cc+tt[i-K]
#        print(i,j,cost1,cost2)
        if cost1<cost2:
            matrix[i][j]=cost1
        else:
            matrix[i][j]=cost2
        if j==0:
            ttt=matrix[i][j]
        else:
            if matrix[i][j]<ttt:
                ttt=matrix[i][j]
        tt[i]=ttt

print(tt[i])
print(matrix)
mm=tt[i]
fout.write (str(mm)+'\n')
fout.close()
