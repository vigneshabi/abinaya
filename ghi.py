d,f=map(int,input().split())
t=[]
for i in range(d+1,f):
    if (i%2==0):
        t.append(i)
print(*t)
