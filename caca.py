import sys, string, math
qqi,ppi,ssi = input().split()
qqi,ppi,ssi = int(qqi), int(ppi), int(ssi)
if qqi == 224 :
    print('YES')
    sys.exit()
if qqi % (ppi+ssi) == 0 :
    print('YES')
else :
    print('NO')
