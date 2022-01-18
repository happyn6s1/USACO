l=[False,False,False,False]
n=0
for i in range(4,2**8):
    if i%2==0:
        l.append(l[i//2])
    elif i%4==1:
        l.append(l[i//4])
    else:
        l.append(not l[i//2])
    if l[-1]:
        n+=1
        #print(i)
        
print(n)
