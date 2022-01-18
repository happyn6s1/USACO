"""
ID: happyn61
LANG: PYTHON3
PROB: gift1
"""
fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')
NP=int(fin.readline().strip())
names=[]
money=[]
for i in range(NP):
    names.append(fin.readline().strip())
    money.append(0)
    
print(names,money)

while True:
    line=fin.readline().strip()
    if line is "":
        break
    m,ng=map(int,fin.readline().strip().split())
    if ng==0:
        continue
    share=m//ng
    print(share,m,ng)
    money[names.index(line)]-=ng*share
    for i in range(ng):
        gname=fin.readline().strip()
        money[names.index(gname)]+=share
#print(names,money)
            
#print(b)



#print(n2%47)
#print(n)
for i in range(NP):
    fout.write (names[i]+ ' ' + str(money[i])+'\n')
    print(names[i] + ' '+str(money[i])+'\n')
    
fout.close()
