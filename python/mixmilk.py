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

fin = open ('mixmilk.in', 'r')
fout = open ('mixmilk.out', 'w')

x=[0,0,0]
y=[0,0,0]
x[0],y[0]=map(int,fin.readline().strip().split())
x[1],y[1]=map(int,fin.readline().strip().split())
x[2],y[2]=map(int,fin.readline().strip().split())

print(x)
print(y)

for i in range(100):
    a=i%3
    b=(i+1)%3
    if y[a]+y[b] <= x[b]:
        y[b]+=y[a]
        y[a]=0
        print(y)
    else:
        y[a]-=x[b]-y[b]
        y[b]=x[b]
        print(y)

print(y)
fout.write (str(y[0])+'\n')
fout.write (str(y[1])+'\n')
fout.write (str(y[2])+'\n')
#    print(names[i] + ' '+str(money[i])+'\n')
    
fout.close()
