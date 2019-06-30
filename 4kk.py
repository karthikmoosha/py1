l=int(input())
k=list(map(int,input().split()))
for i in range(len(k)):
    if k.count(k[i])==1:
        print(k[i])
