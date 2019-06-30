M,K=input().split()
c=input().split()
d=input().split()
e=0
for i in d:
    if i in c:
        e+=1
if e==len(d):
    print("YES")
else:
    print("NO")
