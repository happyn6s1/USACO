import sys
k=0
for line in sys.stdin:
    a,b,c=line.strip().split()
    #print(a,b,c)
    cc=int(c)
    aa=int(a)+cc-1
    bb=int(b)+cc-1
    ans=(aa//cc)*(bb//cc)
    print(str (ans)+"\n")
        
