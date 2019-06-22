b,h=list(map(int,input().split()))
for i in range(b+1,h):
  f=len(str(i))
  a=i
  g=0 
  while a>0:
    d=a%10
    a=a//10
    e=d**f
    g=c+e
  if i==g:
    print(g)
