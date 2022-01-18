l=[0]
for i in range(1,20000):
    k=0
    for x in range(1,i+1):
        for y in range(1,x+1):
            t=(x+y)**2+i**2
            #t2=(x+i)**2+y**2
            #t3=(y+i)**2+x**2
            #print(t,t2,t3)
            if (int(t**(0.5)))**2==t:
                k+=1
                #print(y,x,i)
    l.append(l[-1]+k)
    if l[i]>1000000:    
        print(i,l[i])
        break
    
