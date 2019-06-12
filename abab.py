k,u=map(str,input().split())
c1=0
if len(k)>len(u):
  k,u=u,k
i=0
while i<len(k):
  d1+=(ord(u[i])-ord(k[i]))
  i+=1
for i in range(i,len(u)):
  d1+=ord(u[i])-ord('a')+1
print(d1)
