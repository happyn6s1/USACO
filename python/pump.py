"""
ID: happyn61
LANG: PYTHON3
PROB: pump
"""

from collections import defaultdict

class Graph():
    def __init__(self):
        """
        self.edges is a dict of all possible next nodes
        e.g. {'X': ['A', 'B', 'C', 'E'], ...}
        self.weights has all the weights between two nodes,
        with the two nodes as a tuple as the key
        e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
        """
        self.edges = defaultdict(list)
        self.weights = {}
        self.flows={}
    
    def add_edge(self, from_node, to_node, weight,flow):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight
        self.weights[(to_node, from_node)] = weight
        self.flows[(from_node, to_node)] = flow
        self.flows[(to_node, from_node)] = flow
        
def dijsktra(graph, initial, end, flow):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()
    
    while current_node != end:
        visited.add(current_node)
        
        destinations = graph.edges[current_node]
        #print(current_node,graph.edges)
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            if graph.flows[(current_node, next_node)] < flow:
                continue
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)
        
        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            #return "Route Not Possible"
            return 0
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])
    
    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
#    print(path)
    cost=0
    for i in range(len(path)-1):
        cost+=graph.weights[(path[i], path[i+1])]
    
    return cost

fin = open ('pump.in', 'r')
fout = open ('pump.out', 'w')
#print(dic["4734"])
mn=fin.readline().strip().split()
N=int(mn[0])
M=int(mn[1])
vlist=[]
vcost=[]
graph=Graph()
for i in range(N+1):
    vlist.append(list())
    ll=99999999999999
    vcost.append(ll)
#print(num)
vcost[1]=0
fset=set()
for i in range(M):
    e=fin.readline().strip().split()
#    print(e,int(e[1]))
    alist=[int(e[1]),int(e[2]),int(e[3])]
    vlist[int(e[0])].append(alist)
    alist=[int(e[0]),int(e[2]),int(e[3])]
    vlist[int(e[1])].append(alist)
    if int(e[3]) not in fset:
        fset.add(int(e[3]))
    glist=(int(e[0]),int(e[1]),int(e[2]),int(e[3]))
    graph.add_edge(*glist)
#    print(names[i] + ' '+str(money[i])+'\n')
flist=sorted(fset)

#print(flist)
mm=0
for i in flist:
    #print(i)
    #findshortest(i,vlist)
    myset={1}
    #vcost already done
    n=dijsktra(graph, 1, N,i)
    
    if n==0:
        break
    if i*1000000//n>mm:
        mm=i*1000000//n
    #print(i*1000000//n)    

fout.write (str(mm)+'\n')
fout.close()
