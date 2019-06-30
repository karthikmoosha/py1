k1=int(input())
b1=input().split()
c1=[]
s1=''
for i in range(k1):
    if i%2==0 and int(b1[i])%2==1:
        c1.append(b1[i])
    if i%2==1 and int(b1[i])%2==0:
        c1.append(b1[i])
for i in range(len(c1)-1):
    s1+=c1[i]+" "
print(s1+c1[-1])
