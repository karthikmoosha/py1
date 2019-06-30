M1=int(input())
l1=list(map(int,input().split()))
for i1 in range(0,M1-2):
    for j1 in range(i1+1,M1-1):
        for k1 in range(j1+1,M1):
            if(l1[i1]+l1[j1]==l1[k1]):
                print(l1[i1], l1[j1], l1[k1])
