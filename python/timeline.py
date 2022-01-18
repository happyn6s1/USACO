"""
ID: happyn61
LANG: PYTHON3
PROB: timeline
"""

from collections import defaultdict

class Graph: 
    def __init__(self,vertices): 
  
        self.V = vertices # No. of vertices 
  
        # dictionary containing adjacency List 
        self.graph = defaultdict(list) 
  
    # function to add an edge to graph 
    def addEdge(self,u,v,w): 
        self.graph[u].append((v,w)) 
  
    # A recursive function used by topologicalSort 
    def topologicalSortUtil(self,v,visited,stack): 
  
        # Mark the current node as visited. 
        visited[v] = True
  
        # Recur for all the vertices adjacent to this vertex 
        if v in self.graph.keys(): 
            for node,weight in self.graph[v]: 
                if visited[node] == False: 
                    self.topologicalSortUtil(node,visited,stack) 
  
        # Push current vertex to stack which stores result 
        stack.insert(0,v) 
  
    # The function to do Topological Sort. It uses recursive  
    # topologicalSortUtil() 
    def topologicalSort(self): 
        # Mark all the vertices as not visited 
        visited = [False]*self.V 
        stack =[] 
  
        # Call the recursive helper function to store Topological 
        # Sort starting from all vertices one by one 
        for i in range(self.V):
            #print(i)
            if visited[int(i)] == False: 
                self.topologicalSortUtil(i,visited,stack) 
  
        # Print contents of the stack 
        #print (stack)
        for i in stack:
            for v in self.graph[i]:
                d[v[0]]=max(d[v[0]],d[i]+v[1])
                

fin = open ('timeline.in', 'r')
fout = open ('timeline.out', 'w')
#print(dic["4734"])
NMC=fin.readline().strip().split()
N=int(NMC[0])
M=int(NMC[1])
C=int(NMC[2])
d=[0]+list(map(int,fin.readline().strip().split()))
rr=[0]*(N+1)

#print(d)
#print(rr)
g = Graph(N+1)
for i in range(C):
    ABX=fin.readline().strip().split()
    a=int(ABX[0])
    b=int(ABX[1])
    x=int(ABX[2])
    print(a,b,x)
    g.addEdge(a, b, x)

s=1
g.topologicalSort()
#print(d)

#print(flist)
mm=0
for i in d:
    if i==0:
        continue
    
    fout.write (str(i)+'\n')
fout.close()
