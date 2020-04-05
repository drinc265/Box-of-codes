test=int(input())

colsum=[]
count=0
trace=[]
rows=[]
columns=[]
var=0
k=0
r=[]
x=[]
flag=0

for i in range(test):
	r.append(int(input()))
	for j in range(r[i]):
		x.append(list(map(int, input().split())))

for i in range(len(x)):
	k=k+x[i][count]
	count=count+1
	if (i-var) == (r[flag]-1):
		trace.append(k)
		var=i+1
		count=0
		flag=flag +1
		k=0

var=0
k=0
count=0

for i in range(test):
	for j in range(k,r[var]+k):
		if len(x[j]) != len(set(x[j])):
			count= count+1
		k=j+1
	rows.append(count)
	count=0
	var=var+1
	

count=0
var=0
k=0

for i in range(len(x)):
	for j in range(var,r[k]+var):
		colsum.append(x[j][i-var])
	if len(colsum)!=len(set(colsum)):
		count=count+1
		colsum.clear()
	else:
		colsum.clear()
	if i-var==r[k]-1:
		columns.append(count)
		var=i+1
		k=k+1
		count=0

for i in range(test):
	print("Case #{}: {} {} {}".format(i+1,trace[i],rows[i],columns[i]))