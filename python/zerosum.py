"""
ID: happyn61
LANG: PYTHON3
PROB: zerosum
"""
rr=0
fin = open ('zerosum.in', 'r')
fout = open ('zerosum.out', 'w')
cl=[]
def check(cl,op):
    #print(cl,op)
    oop=op.copy()
    i=0
    n=0
    sign=1
    term=0
    space=False
    ns=0 #(number of space)
    cc=cl.copy()
    for j in range(len(cl)-1):
        
       if oop[j]==3 :
           ns+=1
           oop[j]=sign
           for k in range(ns):
               cc[j-k]*=10
           
           #print(term)
       elif oop[j]==-1:
            ns=0
            n+=sign*term
            term=0
            sign=-1
            
       elif oop[j]==1:
            ns=0
            n+=sign*term
            term=0
            sign=1
       else:
            term=term*10+cc[j]
       #print(j,space,term,n)
       #print(n,term)
    n=cc[0]

    ss=str(cl[0])
    for j in range(len(cl)-1):
        n+=oop[j]*cc[j+1]
        if op[j]==-1:
            t="-"
        elif op[j]==1:
            t="+"
        else:
            t=" "
        t+=str(cl[j+1])
        ss+=t
    #print(n)
    if n==0:
        print(n,op,ss)
        fout.write(ss+"\n")
        return True
    #if n==0:
        #print(op)
    #print(op)
#def dfs(n,v,l,o):
    
def makesum(n,v,l):
    global rr

    #print(n)
    #print(l)
    if n==v-1:
        
        l[n]=3
        #print(l)
        if(check(cl,l)):
            rr+=1
        l[n]=1
        if(check(cl,l)):
            rr+=1#return
        #print(l)
        l[n]=-1
        if(check(cl,l)):
            rr+=1
            
            #print(l)
    else:
        l[n]=3
        makesum(n+1,v,l)
        l[n]=1
        makesum(n+1,v,l)
        l[n]=-1
        makesum(n+1,v,l)
        
       
N = int(fin.readline().strip())
op=[]
for i in range(N):
    cl.append(i+1)
    if i<N-1:
        op.append(0)
print(cl)
makesum(0,N-1,op)
aa=[1,2,3,4,5,6,7]
bb=[-1,3,-1,3,1,3]
#check(aa,bb)
#print(aa)
#print(bb)
print(rr)

                
fout.close()
    
