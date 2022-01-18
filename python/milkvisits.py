"""
ID: happyn61
LANG: PYTHON3
PROB: milk2
"""
import collections
def traverse(node,vlist):
    #print(root)
    #print(trees[root])
    for c in vlist[node]:
        #print(c)
        nn=vls[node]
        #print(nn)
        vls[c]=vls[c].union(vls[node])
        traverse(c,vlist)

        
fin = open ('milkvisits.in', 'r')
fout = open ('milkvisits.out', 'w')
NM=fin.readline().strip().split()
N=int(NM[0])
M=int(NM[1])
taste=("0 "+fin.readline().strip()).split()

print(taste)

root=0
vlist=[]
vls=[]
for i in range(N+1):
    vlist.append(set())
    vls.append(set())
    vls[i].add(int(taste[i]))
#vls[1].add(2)
trees= collections.defaultdict(dict)
for i in range(N-1):
    XY=fin.readline().strip().split()
    
    parent=int(XY[0])
    child=int(XY[1])

    vlist[parent].add(child)
    #vlist[child].add(parent)
    
#print(vlist,vls)
node=1
traverse(node,vlist)
print(vls)

res=""        
for i in range(M):
    ABC=fin.readline().strip().split()
    A=int(ABC[0])
    B=int(ABC[1])
    C=int(ABC[2])
    

    

fout.close()
