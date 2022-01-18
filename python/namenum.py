"""
ID: happyn61
LANG: PYTHON3
PROB: namenum
"""

dic={}
with open('dict.txt') as f:
    content = f.readlines()
    for c in content:
        cl=list(c.strip())
        code=""
        for i in range(len(cl)):
            if cl[i]<='P':
                nn=(ord(cl[i])-ord('A')+3)//3+1
            if cl[i]>'P':
                nn=(ord(cl[i])-ord('A')+2)//3+1
            code+=str(nn)
        if code in dic:
            dic[code].append(c.strip())
        else:
            a=[c.strip()]
            dic[code]=a
        if c.strip()=="KRISTOPHER":
            print(code,cl)
#print(dic)
fin = open ('namenum.in', 'r')
fout = open ('namenum.out', 'w')
#print(dic["4734"])
num=fin.readline().strip()
#print(num)
if num in dic:
#    print("in")
    ll=dic[num]
    print(ll)
#print(m1,m2)
else:
    ll=["NONE"]
current=0
color='w'
start=False
k=0
cw=0

for i in ll:
    fout.write (i+'\n')
    
#    print(names[i] + ' '+str(money[i])+'\n')
    
fout.close()
