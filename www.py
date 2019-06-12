from itertools import combinations
s2,v=map(int,input().split())
u=len(str(s2))
y=list(combinations(str(s2),u-v))
y=(sorted(y))
x="".join(y[0])
print(s)
