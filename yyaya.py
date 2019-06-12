aa21=int(input())
ki=list(map(int,input().split()))
cd=0
for i in range(len(ki)-2):
    for j in range(i+1,len(ki)-1):
        for n in range(j+1,len(li)):
            if ki[i]<ki[j]<ki[n] and i<j<n:
                cd=cd+1
print(cd)
