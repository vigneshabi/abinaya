h11=input()
h11=int(h11)
v1=[]
for j in range(0,h11):  
    n11=input()
    v11.append(n11)
f11=[]
for j in zip(*v11):
    if j.count(j[0])==len(j): 
        f11.append(j[0])
    else:
        break
print(''.join(f11))
