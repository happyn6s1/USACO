"""
ID: happyn61
LANG: PYTHON3
PROB: cowmbat
"""
import collections
import sys
class NumArray(object):

	def __init__(self, nums):
		self.l = len(nums)
		self.tree = [0]*self.l + nums
		for i in range(self.l - 1, 0, -1):
			self.tree[i] = self.tree[i<<1] + self.tree[i<<1|1]
	
	def update(self, i, val):
		n = self.l + i
		self.tree[n] = val
		while n > 1:
			self.tree[n>>1] = self.tree[n] + self.tree[n^1]
			n >>= 1
		
	
	def sumRange(self, i, j):
		m = self.l + i
		n = self.l + j
		res = 0
		while m <= n:
			if m & 1:
				res += self.tree[m]
				#res +=1
				print(res)
				m += 1
			m >>= 1
			if n & 1 ==0:
				res += self.tree[n]
				#res +=1
				print(res)
				n -= 1
			n >>= 1
		return res

        
fin = open ('haybales.in', 'r')
fout = open ('haybales.out', 'w')
NQ=(fin.readline().strip().split())
N=int(NQ[0])
Q=int(NQ[1])

mm=0
#for each mod min and max
#ma = [ [ 0 for i in range(2) ] for j in range(7) ]
#ml= [int(fin.readline().strip()) for j in range(N)]
ml=[int(i) for i in fin.readline().strip().split()]
print (ml)
#p= [0 for j in range(N)]
#pst= [0 for j in range(N+1)]

#print(N)
ml.sort()
na=NumArray(ml)
print(na.sumRange(2,7))
ss=0
nn=99999
nnn=-1

'''
    ml=int(fin.readline().strip())
    ss=(ss+ml)%7
    pre[i+1]=ss
    if ma[ss][0]==0:
        ma[ss][0]=i+1
        ma[ss][1]=i+1
    else:
        if (i+1) < ma[ss][0]:
            ma[ss][0]=i+1
        elif ma[ss][1] < (i+1):
            ma[ss][1]=i+1

for i in range(7):
    print(i)
    if ma[i][1]-ma[i][0]>mm:
        mm=ma[i][1]-ma[i][0]
'''

                                   
print(mm)
fout.write (str(mm)+'\n')
fout.close()
