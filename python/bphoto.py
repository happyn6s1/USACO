"""
ID: happyn61
LANG: PYTHON3
PROB: bphoto
"""

def findandinsert(ll,lr,m,k):
    if len(ll)==0:
        ll.append(m)
        return
    
    lo=0
    hi=len(ll)
    ist=0
    if m<ll[0]:
        ll.insert(0,m)
        ist=0
    elif m>ll[-1]:
        ll.append(m)
        ist=len(ll)-1
    else:
        while lo<hi-1:
            mi=(hi+lo)//2
            if m>ll[mi]:
                lo=mi
            else:
                hi=mi
            
        ll.insert(hi,m)
        ist=hi
    #print(ll,ist)
    if  ((len(ll)-ist-1)>2*ist or ist > 2*(len(ll)-ist-1)):
        lr.append(k)
        print(k)
fin = open ('bphoto.in', 'r')
fout = open ('bphoto.out', 'w')

#cowlist=[]
n=int(fin.readline().strip())

l=[]
for i in range(n):
    l.append((int(fin.readline().strip()),i))
    
l.sort(reverse=True)
#print(l)
smax=0
rl=[]
ll=[]
for i in range(n):
    k=l[i][0]
    m=l[i][1]
    findandinsert(ll,rl,m,k)
        
#print(len(rl),rl)
fout.write (str(len(rl))+'\n')
#fout.write (str(y[1])+'\n')
#fout.write (str(y[2])+'\n')
#    print(names[i] + ' '+str(money[i])+'\n')
    
fout.close()
