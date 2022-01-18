l=[set()]
import math
l.append({1})
i=2
n=20
def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)
while i<n:
    
    s=l[-1].copy()
    s.add(i+2)
    for j in range(1,i-1):
        #print(i,l,s,j,i-j,l)
        for a in l[j]:
            for b in l[i-j]:
                #print(a,b)
                s.add(lcm(a,b))
    l.append(s)
    i+=1

for t in l:
    print(len(t))

              
    
    
