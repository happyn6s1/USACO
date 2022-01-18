"""
ID: happyn61
LANG: PYTHON3
PROB: palsquare
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
    
fin = open ('palsquare.in', 'r')
fout = open ('palsquare.out', 'w')
#print(dic["4734"])
base=int(fin.readline().strip())
#print(num)
for i in range(1,301):
    if ispalindromel(n2lbase(i*i,base)):
        cl=n2lbase(i,base)
        cl.reverse()
        print("".join(cl)+" "+"".join(n2lbase(i*i,base)))
        #print(str(n2lbase(i,base)))
        fout.write ("".join(cl)+" "+"".join(n2lbase(i*i,base))+'\n')
    
#    print(names[i] + ' '+str(money[i])+'\n')
    
fout.close()
