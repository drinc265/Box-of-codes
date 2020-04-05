def split(x, n): 
    a=[]

    if (x % n == 0): 
        for i in range(n): 
            a.append(x/n)
        return a         
    else: 
        zp = n - (x % n) 
        pp = x//n 
        for i in range(n): 
            if(i>= zp): 
                a.append(pp+1) 
            else: 
                a.append(pp)
        return a

test=int(input())
a=[]
s=''
temp=[]
for _ in range(test):
	a.append(list(map(int, input().split())))
for i in range(test):
	mat=[]
	x=split(a[i][1],a[i][0])
	for _ in range(a[i][0]):
		for j in range(1,a[i][0]+1):
			temp.append(j)
		mat.append(temp)
		temp=[]
	for l in range(a[i][0]):
		mat[l][mat[l].index(x[l])]=mat[l][l]
		mat[l][l]=int(x[l])
		if len(mat[l])!=len(set(mat[l])):
			s='IMPOSSIBLE'
		else:
			s='POSSIBLE'
	
	print("Case #{}: {}".format(i+1,s))
	if s=='POSSIBLE':
		for j in range(a[i][0]):
			for k in range(a[i][0]):
				print(mat[j][k], end=' ')
			print()
	mat.clear()