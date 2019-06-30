k1=int(input())
b1=input()
c1=''
for i in b1:
    if i in c1 and i!=" ":
        print(int(i))
        break
    else:
        c1+=i
if c1==b1:
    print("unique")
