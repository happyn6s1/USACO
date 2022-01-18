"""
ID: happyn61
LANG: PYTHON3
PROB: sort
"""

    
fin = open ('sort.in', 'r')
fout = open ('sort.out', 'w')
#print(dic["4734"])
N=int(fin.readline().strip())

sl=[]
for i in range(N):
    sl.append([int(fin.readline().strip()),i])
sl.sort()

ma=0
mn=2000
for i in range(N):
    ma=max(sl[i][1]-i,ma)
print(ma+1)
#    print(names[i] + ' '+str(money[i])+'\n')
fout.write (str(ma+1)+'\n')  
fout.close()
