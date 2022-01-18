"""
ID: happyn61
LANG: PYTHON3
PROB: friday
"""
def compare(comb,key):
    for i in range(3):
        if abs(comb[i]-key[i])<=2 or abs(comb[i]-key[i])>=48:
            continue
        else:
            return False
        
                                         
    return True

fin = open ('relay.in', 'r')
fout = open ('relay.out', 'w')
n=int(fin.readline().strip())
t=0
fwd=[0]
noloop=[]
yesloop=[]
for i in range(n):
    m=int(fin.readline().strip())
    fwd.append(m)

for j in range(n):
    i=j+1
    if fwd[i]==0 or fwd[i] in noloop:
        t+=1
        noloop.append(i)
    elif fwd[i] in yesloop:
        yesloop.append(i)
    else:
        loopy=[]
        nl=False
        while(fwd[i] not in loopy):
            loopy.append(fwd[i])
            
            i=fwd[i]
            if fwd[i]==0 or fwd[i] in noloop:
                t+=1
                nl=True
                break
            elif fwd[i] in yesloop:
                break
        if nl:
            noloop.append(i)
        else:
            yesloop.append(i)
        
print(fwd,noloop,yesloop)
print(t)
fout.write (str(t)+'\n')

fout.close()
