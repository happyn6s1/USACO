"""
ID: happyn61
LANG: PYTHON3
PROB: time
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

        
fin = open ('time.in', 'r')
fout = open ('time.out', 'w')
NM=fin.readline().strip().split()
N=int(NM[0])
M=int(NM[1])
C=int(NM[2])
m=[int(x) for x in fin.readline().strip().split()]

from collections import defaultdict 
  
# This class represents a directed graph using 
# adjacency list representation 
class Graph: 
  
    # Constructor 
    def __init__(self): 

        # default dictionary to store graph 
        self.graph = defaultdict(list)
        self.cycles= []
        self.weights= []
    # function to add an edge to graph
    def printcycles(self):
        return self.cycles
    def addEdge(self, u, v): 
        self.graph[u].append(v)
    def addweights(self, l): 
        self.weights=l.copy()
    
  
    # A function used by DFS 
    def DFSUtil(self, v, visited, start ,path): 
  
        # Mark the current node as visited  
        # and print it
        path.append(v)
        visited[v] = True
        print(v, end = ' ') 
  
        # Recur for all the vertices  
        # adjacent to this vertex 
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.DFSUtil(i, visited , start,path)
            elif i==start:
                print("found one",path)
                #return
  
    # The function to do DFS traversal. It uses 
    # recursive DFSUtil() 
    def DFS(self, v): 
  
        # Mark all the vertices as not visited 
        visited = [False] * (len(self.graph)) 
  
        # Call the recursive helper function  
        # to print DFS traversal
        path=[]
        cycles=self.DFSUtil(v, visited, v,path)
    def BFS(self, s): 
  
        # Mark all the vertices as not visited 
        visited = [False] * (len(self.graph)) 
        start=s
        # Create a queue for BFS 
        queue = [] 
  
        # Mark the source node as  
        # visited and enqueue it 
        queue.append(s) 
        visited[s] = True
  
        while queue: 
  
            # Dequeue a vertex from  
            # queue and print it 
            s = queue.pop(0) 
            print (s, end = " ") 
  
            # Get all adjacent vertices of the 
            # dequeued vertex s. If a adjacent 
            # has not been visited, then mark it 
            # visited and enqueue it 
            for i in self.graph[s]: 
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True
                elif i==start:
                    print("found one")
    def printAllPathsUtil(self, u, d, visited, path,start): 
  
        # Mark the current node as visited and store in path 
        visited[u]= True
        path.append(u) 
  
        # If current vertex is same as destination, then print 
        # current path[] 
        if u == start: 
            #print (u,d,start,visited,path)
            w=self.weights[start]
            for i in path:
                w+=self.weights[i]
            self.cycles.append([len(path),w])
                
        else: 
            # If current vertex is not destination 
            #Recur for all the vertices adjacent to this vertex 
            for i in self.graph[u]: 
                if visited[i]==False: 
                    self.printAllPathsUtil(i, d, visited, path,start) 
                      
        # Remove current vertex from path[] and mark it as unvisited 
        path.pop() 
        visited[u]= False
   
   
    # Prints all paths from 's' to 'd' 
    def printAllPaths(self,s, d): 
  
        # Mark all the vertices as not visited 
        visited =[False]*(len(self.graph))  
  
        # Create an array to store paths 
        path = [] 
  
        # Call the recursive helper function to print all paths 
        self.printAllPathsUtil(s, d,visited, path)
    def printAllPathsloop(self,s): 
  
        # Mark all the vertices as not visited 
        visited =[False]*(len(self.graph))  
  
        # Create an array to store paths 
        path = [] 
  
        # Call the recursive helper function to print all paths
        for d in self.graph[s]:
            #visited[s]=True
            self.printAllPathsUtil(d, s,visited, path,s)        
# Driver code 
  
# Create a graph given  
# in the above diagram 
g = Graph()

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

#print(N,M,C,m)
ll=[]
for i in range(M):
    [a,b]=[int(x) for x in fin.readline().strip().split()]
    #print(a,b)
    #g.addEdge(a-1,b-1)
    ll.append((a,b))
#g.addweights(m)

#g.printAllPathsloop(0)
#cy=g.printcycles()
#print(cy)
n=800
l=[[-1 for j in range(N+1)] for i in range(n+1)]
l[0][1]=0
#print(ll,l)
mm=0
for i in range(0,n):
    for j in range(M):
        a=ll[j][0]
        b=ll[j][1]
        #print(a,b,l[i+1][b],l[i][a]+m[a-1])
        #print(a,b,l[i][a])
        if l[i][a]>=0:
            l[i+1][b]=max(l[i+1][b],l[i][a]+m[b-1])
    #print(l[i+1])
    mm=max(mm,l[i+1][1]-C*(i+1)*(i+1))
    #print(i,mm)
        #print(l)
print(mm)
#print(l)
                     
'''
mm=0
ct=0
nt=True
d=dict()
for i in cy:
    if i[0] in d:
        if i[1] > d[i[0]]:
            d[i[0]]=i[1]
    else:
        d[i[0]]=i[1]

        
        
while nt:
    z=0 #positive to go

    for i in cy:
        x=i[1]-C*(i[0]+ct)**2
        if x>z:
            z=x
            cc=i[0]
            print(z,cc)
    if z<=0:
        nt=False
    else:
        mm+=z
        ct+=cc
zz=[0]
ww=[0]
cc=0
while nt:
    tt=0
    ct+=1
    x=0
    for i in d:
        if i<=ct:
            x=max(zz[ct-i]+d[i],x)
    zz.append(x)
    if (x > (ct)**2*C):
        cc=0
    else:
        cc+=1
    ww.append(x-(ct)**2*C) 
    if cc>1000:
        nt=False
#print(zz)
#print(ww)
mm=max(ww)
#print(mm)
'''
fout.write (str(mm)+'\n')
fout.close()
