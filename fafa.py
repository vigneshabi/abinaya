value3=int(input())
value62=[int(i) for i in input().split()]
result=0
for i in range(value3):
	for j in range(i):
		if value62[j]<value62[i]:
			result+=value62[j]
print(result)
