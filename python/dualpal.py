"""
ID: happyn61
LANG: PYTHON3
PROB: dualpal
"""
def n2lbase(n,base):
    ss="ABCDEFGHIJKLMNOPQ"
    l=[]
    while n>0:
        m=n%base
        if m>9:
            l.append(ss[m-10])
        else:
            l.append(str(m))
        n=n//base
	#print (l)
    return l
def ispalindromel(l):
	ispalindrome=True
	for i in range(0,len(l)//2+1):
		if l[i] != l[len(l)-1-i]:
			ispalindrome=False
			break
	return ispalindrome
    
fin = open ('dualpal.in', 'r')
fout = open ('dualpal.out', 'w')
#print(dic["4734"])
NS=fin.readline().strip().split()
N=int(NS[0])
S=int(NS[1])
mm=0
#print(num)
for i in range(S+1,99999999):
    once=False
    done=False
    for j in range(2,11):
        if ispalindromel(n2lbase(i,j)) and once:
            mm+=1
            print(i)
            fout.write (str(i)+'\n')
            done=True
            break
        elif ispalindromel(n2lbase(i,j)):
            once=True
        
        if done:
            break
        #print(str(n2lbase(i,base)))
    if mm>=N:
        break
#    print(names[i] + ' '+str(money[i])+'\n')
    
fout.close()
