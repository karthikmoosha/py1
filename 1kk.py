l = int(input())
k = list(map(int,input().split()))
r = []
for i in range(len(k)):
    if k.count(k[i]) > 1:
        if k[i] not in r:
            r.append(k[i])
r.sort()
if len(r)==0:
    print("unique")
else:
    print(" ".join([str(elem) for elem in r]))
