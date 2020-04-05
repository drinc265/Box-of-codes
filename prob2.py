test=int(input())
s=[]
temp=[]
final=[]
for i in range(test):
	s.append(input())

for i in range(len(s)):
	temp.append(list(s[i]))

for i in range(len(temp)):
	for j in range(len(temp[i])):
		x=int(temp[i][j])
		for k in range(x):
			temp[i][j]=temp[i][j]+')'
			temp[i][j]='(' + temp[i][j]

for i in range(len(temp)):
	final.append(''.join([str(elem) for elem in temp[i]]))

for i in range(len(final)):
	while final[i].find(')(')!=-1:
		final[i]=final[i].replace(')(','')

for i in range(len(final)):
	print("Case #{}: {}".format(i+1,final[i]))