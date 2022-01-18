"""
ID: happyn61
LANG: PYTHON3
PROB: square
"""

fin = open ('square.in', 'r')
fout = open ('square.out', 'w')

l1= list(map(int,fin.readline().strip().split()))
l2=list(map(int,fin.readline().strip().split()))
rr=max(max(l1[2],l2[2])-min(l1[0],l2[0]),max(l1[3],l2[3])-min(l1[1],l2[1]))
print(rr*rr)        
fout.write(str(rr*rr)+"\n")
                
fout.close()
    
