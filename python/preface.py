"""
ID: happyn61
LANG: PYTHON3
PROB: preface
"""

def printRoman(number): 
    num = [1, 4, 5, 9, 10, 40, 50, 90,  
           100, 400, 500, 900, 1000] 
    sym = ["I", "IV", "V", "IX", "X", "XL",  
           "L", "XC", "C", "CD", "D", "CM", "M"] 
    i = 12
    while number: 
        div = number // num[i] 
        number %= num[i] 
  
        while div: 
            #print(sym[i], end = "") 
            div -= 1
        i -= 1

def checkRoman(l,number): 
    num = [1, 4, 5, 9, 10, 40, 50, 90,  
           100, 400, 500, 900, 1000] 
    sym = ["I", "IV", "V", "IX", "X", "XL",  
           "L", "XC", "C", "CD", "D", "CM", "M"] 
    i = 12
    while number: 
        div = number // num[i] 
        number %= num[i] 
  
        while div: 
            #print(sym[i], end = "")
            l[i]+=1
            div -= 1
        i -= 1

fin = open ('preface.in', 'r')
fout = open ('preface.out', 'w')
#print(dic["4734"])
N=int(fin.readline().strip())

nl=[0]*13
for i in range(1,N+1):
    checkRoman(nl,i)
        
print(nl)
sym = ["I", "IV", "V", "IX", "X", "XL",  
    "L", "XC", "C", "CD", "D", "CM", "M"]

s = ["I","V","X","L","C","D","M"]
nl2=[[0,s[i]] for i in range(7)]

print(nl2)
nl2[0][0]=nl[0]+nl[1]+nl[3]
nl2[1][0]=nl[1]+nl[2]
nl2[2][0]=nl[3]+nl[4]+nl[5]+nl[7]
nl2[3][0]=nl[5]+nl[6]
nl2[4][0]=nl[7]+nl[8]+nl[9]+nl[11]
nl2[5][0]=nl[9]+nl[10]
nl2[6][0]=nl[11]+nl[12]

print(nl2)
#nl2.sort(reverse = True)
for i in range(7):
    if nl2[i][0]>0:
        print(nl2[i][1],nl2[i][0])
        fout.write (nl2[i][1]+" "+str(nl2[i][0])+"\n")
    
fout.close()
