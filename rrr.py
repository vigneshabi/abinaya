s=list(map(int,input().split()))
e=q[1]
w=list(map(int,input().split()))
q=0
x=len(w)
for i in range(0,x):
    if(i<e):
        q=q+w[i]
print(q)
