"""
ID: happyn61
LANG: PYTHON3
PROB: moocast
"""
from collections import defaultdict 
import sys 
import math  
class Heap(): 
  
    def __init__(self): 
        self.array = [] 
        self.size = 0
        self.pos = [] 
    
    def newMinHeapNode(self, v, dist): 
        minHeapNode = [v, dist] 
        return minHeapNode 
  
    # A utility function to swap two nodes of  
    # min heap. Needed for min heapify 
    def swapMinHeapNode(self, a, b): 
        t = self.array[a] 
        self.array[a] = self.array[b] 
        self.array[b] = t 
  
    # A standard function to heapify at given idx 
    # This function also updates position of nodes  
    # when they are swapped. Position is needed  
    # for decreaseKey() 
    def minHeapify(self, idx): 
        smallest = idx 
        left = 2 * idx + 1
        right = 2 * idx + 2
  
        if left < self.size and self.array[left][1] < \
                                self.array[smallest][1]: 
            smallest = left 
  
        if right < self.size and self.array[right][1] < \
                                self.array[smallest][1]: 
            smallest = right 
  
        # The nodes to be swapped in min heap  
        # if idx is not smallest 
        if smallest != idx: 
  
            # Swap positions 
            self.pos[ self.array[smallest][0] ] = idx 
            self.pos[ self.array[idx][0] ] = smallest 
  
            # Swap nodes 
            self.swapMinHeapNode(smallest, idx) 
  
            self.minHeapify(smallest) 
  
    # Standard function to extract minimum node from heap 
    def extractMin(self): 
  
        # Return NULL wif heap is empty 
        if self.isEmpty() == True: 
            return
  
        # Store the root node 
        root = self.array[0] 
  
        # Replace root node with last node 
        lastNode = self.array[self.size - 1] 
        self.array[0] = lastNode 
  
        # Update position of last node 
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1
  
        # Reduce heap size and heapify root 
        self.size -= 1
        self.minHeapify(0) 
  
        return root 
  
    def isEmpty(self): 
        return True if self.size == 0 else False
  
    def decreaseKey(self, v, dist): 
  
        # Get the index of v in  heap array 
  
        i = self.pos[v] 
  
        # Get the node and update its dist value 
        self.array[i][1] = dist 
  
        # Travel up while the complete tree is not  
        # hepified. This is a O(Logn) loop 
        while i > 0 and self.array[i][1] < \
                    self.array[(i - 1) // 2][1]: 
  
            # Swap this node with its parent 
            self.pos[ self.array[i][0] ] = (i-1)//2
            self.pos[ self.array[(i-1)//2][0] ] = i 
            self.swapMinHeapNode(i, (i - 1)//2 ) 
  
            # move to parent index 
            i = (i - 1) // 2; 
  
    # A utility function to check if a given vertex 
    # 'v' is in min heap or not 
    def isInMinHeap(self, v): 
  
        if self.pos[v] < self.size: 
            return True
        return False
  
  
def printArr(parent, n): 
    for i in range(1, n): 
        print ("% d - % d" % (parent[i], i) )
  
  
class Graph(): 
  
    def __init__(self, V): 
        self.V = V 
        self.graph = []
  
    # Adds an edge to an undirected graph 
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w]) 
    def find(self, parent, i): 
        if parent[i] == i: 
            return i 
        return self.find(parent, parent[i]) 
  
    # A function that does union of two sets of x and y 
    # (uses union by rank) 
    def union(self, parent, rank, x, y): 
        xroot = self.find(parent, x) 
        yroot = self.find(parent, y) 
  
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
    def KruskalMST(self): 
  
        result =[] #This will store the resultant MST 
        m=0
        i = 0 # An index variable, used for sorted edges 
        e = 0 # An index variable, used for result[] 
  
            # Step 1:  Sort all the edges in non-decreasing  
                # order of their 
                # weight.  If we are not allowed to change the  
                # given graph, we can create a copy of graph 
        self.graph =  sorted(self.graph,key=lambda item: item[2]) 
  
        parent = [] ; rank = [] 
  
        # Create V subsets with single elements 
        for node in range(self.V): 
            parent.append(node) 
            rank.append(0) 
      
        # Number of edges to be taken is equal to V-1 
        while e < self.V -1 : 
  
            # Step 2: Pick the smallest edge and increment  
                    # the index for next iteration
            #print(i)
            u,v,w =  self.graph[i] 
            i = i + 1
            x = self.find(parent, u) 
            y = self.find(parent ,v) 
  
            # If including this edge does't cause cycle,  
                        # include it in result and increment the index 
                        # of result for next edge 
            if x != y: 
                e = e + 1     
                result.append([u,v,w]) 
                self.union(parent, rank, x, y)             
            # Else discard the edge 
  
        # print the contents of result[] to display the built MST 
        #print "Following are the edges in the constructed MST"
        for u,v,weight  in result:
            if m==0:
                m=weight
            else:
                m=max(m,weight)
            #print str(u) + " -- " + str(v) + " == " + str(weight) 
        return m
    def PrimMST(self):
        maxint=9999999999999999
        # Get the number of vertices in graph 
        V = self.V   
          
        # key values used to pick minimum weight edge in cut 
        key = []    
          
        # List to store contructed MST 
        parent = []  
  
        # minHeap represents set E 
        minHeap = Heap() 
  
        # Initialize min heap with all vertices. Key values of all 
        # vertices (except the 0th vertex) is is initially infinite 
        for v in range(V): 
            parent.append(-1) 
            key.append(maxint) 
            minHeap.array.append( minHeap.newMinHeapNode(v, key[v]) ) 
            minHeap.pos.append(v) 
  
        # Make key value of 0th vertex as 0 so  
        # that it is extracted first 
        minHeap.pos[0] = 0
        key[0] = 0
        minHeap.decreaseKey(0, key[0]) 
        w=0
        m=0
        # Initially size of min heap is equal to V 
        minHeap.size = V; 
  
        # In the following loop, min heap contains all nodes 
        # not yet added in the MST. 
        while minHeap.isEmpty() == False: 
  
            # Extract the vertex with minimum distance value 
            newHeapNode = minHeap.extractMin() 
            u = newHeapNode[0]
            #print(newHeapNode)
            w+= newHeapNode[1]
            m=max(m,newHeapNode[1])
            # Traverse through all adjacent vertices of u  
            # (the extracted vertex) and update their  
            # distance values 
            for pCrawl in self.graph[u]: 
  
                v = pCrawl[0] 
  
                # If shortest distance to v is not finalized  
                # yet, and distance to v through u is less than 
                # its previously calculated distance 
                if minHeap.isInMinHeap(v) and pCrawl[1] < key[v]: 
                    key[v] = pCrawl[1] 
                    parent[v] = u 
  
                    # update distance value in min heap also 
                    minHeap.decreaseKey(v, key[v]) 
  
        #printArr(parent, V) 
        #print(m)
        return m
  
# Driver program to test the above functions 
fin = open ('moocast.in', 'r')
fout = open ('moocast.out', 'w')

#cowlist=[]
def findedge(i,j,n,m,nc,mc):
    l=[]
    if i>0:
        l.append((mc[j],i-1,j,(i,j,i-1,j)))
    if j>0:
        l.append((nc[i],i,j-1,(i,j,i,j-1)))
    if i<n-1:
        #print(m,n,i,j,mc,nc)
        l.append((mc[j],i+1,j,(i,j,i+1,j)))
    if j<m-1:
        l.append((nc[i],i,j+1,(i,j,i,j+1)))
    return l

from datetime import datetime
#print(datetime.now())
N=int(fin.readline().strip())
l=[]
for i in range(N):
    l.append(tuple(map(int,fin.readline().strip().split())))
#print(l)


#print(datetime.now())
graph = [[] for i in range(N)]
hi=0
edge=[]
for i in range(N-1):
    for j in range(i+1,N):
        
        if i==j:
            continue
        #graph[i].append((j,(l[i][0]-l[j][0])**2+(l[i][1]-l[j][1])**2))
        dist=(l[i][0]-l[j][0])**2+(l[i][1]-l[j][1])**2
        edge.append((dist,i,j))
        #graph[j].append((i,(l[i][0]-l[j][0])**2+(l[i][1]-l[j][1])**2))
        #print(graph,N)
        #hi=max(hi,(l[i][0]-l[j][0])**2+(l[i][1]-l[j][1])**2)
#print(datetime.now())
#print(l)
hi=1
#print(graph)
#smax=graph.PrimMST()
#smax=graph.KruskalMST()
lo=0
parent=[i for i in range(N)]
rank=[0 for i in range(N)]
def find(i):


    if parent[i] != i: 
        parent[i]=find(parent[i]) 
    return parent[i] 

        # A utility function to do union of two subsets 
def union(xx,yy): 
    x=find(xx)
    y=find(yy)
    if rank[x]>rank[y]:
        parent[y]=x
    elif rank[y]>rank[x]:
        parent[x]=y
    else:
        parent[y]=x
        rank[x]+=1

def dfs(m):
    visited=[False for i in range(N)]
    
    stack=[0]
    visited[0]=True
    while stack:
        #print(m,stack)
        p=stack.pop()
        for i,w in graph[p]:
            if not visited[i] and w<=mi:
                visited[i]=True
                stack.append(i)

    k=0
    #print(m,visited)
    for t in visited:
        if t:
            k+=1
    if k<N:
        return False
    return True
ans=hi
k=N
edge.sort()
for ans,i,j in edge:
    if find(i)!=find(j):
        k-=1
        if k==1:
            break
        union(i,j)
    #print(ans,i,j,parent,k)
        
  
		
print(ans)
#smax=0
#print(datetime.now())
#print(len(rl),rl)
#smax=math.ceil(ans**0.5)
fout.write (str(ans)+'\n')
#fout.write (str(y[1])+'\n')
#fout.write (str(y[2])+'\n')
#    print(names[i] + ' '+str(money[i])+'\n')
    
fout.close()
