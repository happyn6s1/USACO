nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
l=[]
k=-1
for i in range(len(nums)):
	for j in range(len(nums[i])):
		if i+j>k:
			tl=[nums[i][j]]
			l.append(tl)
			k+=1
		else:
			l[i+j].append(nums[i][j])

ll=[]
for i in range(len(l)):
	l[i].reverse()
	ll=ll+l[i]
print(ll)
