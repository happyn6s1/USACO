d1={}
    
with open("data1.csv") as f1:
    f1.readline()
    for line in f1:
        l=line.replace(",","").strip().split()
        
        d1[l[0]]=float(l[2])
import heapq
speedhq=[]
with open("data2.csv") as f2:
    f2.readline()
    for line in f2:
        l=line.replace(",","").strip().split()
        if l[0] in d1:
            heapq.heappush(speedhq,(d1[l[0]]*float(l[2])/float(l[1]),l[0]))
while speedhq:
    i=heapq.heappop(speedhq)
    print(i[1],"{0:0.2f}".format(i[0]))
