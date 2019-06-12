import math
import functools
a,b = map(int,input().split())
arr = list(map(int,input().split()))
for i in range(q):
	c,d = map(int,input().split())
	d = functools.reduce(math.gcd,arr[l-1:m])
	print(d)
  
