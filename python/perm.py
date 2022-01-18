l=[1,1,2,6,24,120,720,5040,40320,362880]
n=10
k=1000000-1
d=[str(i) for i in range(n)]

ll=[]
for i in range(n-1,-1,-1):
    div=k//l[i]
    ll.append(d[div])
    del d[div]
    k=k%l[i]
print( "".join(ll))
