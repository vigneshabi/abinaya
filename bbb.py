h1=input()
h1=int(h1)
v1=[]
for j in range(0,h1):  
    n1=input()
    v1.append(n1)
f1=[]
for j in zip(*v1):
    if j.count(j[0])==len(j): 
        f1.append(j[0])
    else:
        break
print(''.join(f1))
