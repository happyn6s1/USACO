"""
ID: happyn61
LANG: PYTHON3
PROB: skidesign
"""

    
fin = open ('skidesign.in', 'r')
fout = open ('skidesign.out', 'w')
#print(dic["4734"])
N=int(fin.readline().strip())

sl=[]
for i in range(0,101):
    sl.append(0)

ma=0
mn=2000
for i in range(N):
    n=int(fin.readline().strip())
    sl[n]+=1
    if n>ma:
        ma=n
    if  n< mn:
        mn=n

i=mn
j=ma
s1=0
s2=0
sa=0
sb=0

#print(s1,s2,sa+sb)        
mm=0
nnn=999999999999
print(sa+sb)
for j in range(84):
   
    mm=0
    for i in range(101):
        
        if i<j:
            mm+=sl[i]*(i-j)**2
        if i>j+17:
            mm+=sl[i]*(j+17-i)**2
    if mm< nnn:
        nnn=mm
print(mm,nnn)
#    print(names[i] + ' '+str(money[i])+'\n')
fout.write (str(nnn)+'\n')  
fout.close()
