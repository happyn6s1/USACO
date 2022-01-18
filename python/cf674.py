import sys
k=0
for line in sys.stdin:
    if k==0:
        N=int(line)
    else:
        a,b=line.strip().split()
        n=int(a)
        m=int(b)
        if n<=2:
            print("1")
        else:
            print(str((n-3)//m+2)+"\n")
    k+=1
        
