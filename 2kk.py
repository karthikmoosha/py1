l=int(input())
k=list(map(int,input().split()))
k.sort(reverse=True)
c=0
for i in range(0,int(len(k))):
    c=(c*10)+k[i]
print(c)
