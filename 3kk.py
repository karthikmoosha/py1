l=int(input())
k=list(map(int,input().split()))
b=[]
for i in range(len(k)):
    if i==k[i]:
        b.append(i)
        
if len(b)>=1:
    print(*b)
else:
    print(-1)
