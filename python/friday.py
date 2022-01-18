"""
ID: happyn61
LANG: PYTHON3
PROB: friday
"""
def leap(year):
    if year%4==0:
        if year%100 !=0:
            return True
        elif year %400==0:
            return True
        else:
            return False
    return False

fin = open ('friday.in', 'r')
fout = open ('friday.out', 'w')
N=int(fin.readline().strip())
days=[31,31,28,31,30,31,30,31,31,30,31,30]
count=[0,0,0,0,0,0,0]
prev=6-31
for i in range(N):
    for month in range(12):
        
        if month == 2 and leap(1900+i):
            current=(prev+days[month]+1)%7
        else:
            current=(prev+days[month])%7
        prev=current
        count[current]+=1

print(count)

fout.write (str(count[6]))
    
for i in {0,1,2,3,4,5}:
    fout.write (' '+str(count[i]))
    
fout.write('\n')
#    print(names[i] + ' '+str(money[i])+'\n')
    
fout.close()
