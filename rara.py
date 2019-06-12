import math
ss=int(input())
jj=math.log10(ss)/math.log10(2)
if math.ceil(jj)==math.floor(jj):
	print(0)
else:
	mm=(ss-1)//2
	nn=mm*2
	print(ss-nn)
  
