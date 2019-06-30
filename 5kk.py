kk=list(map(str,input()))
aa=dd=0
for i in range(0,len(kk)-1):
    bb=kk[i]
    if int(bb)!=0:
        for j in range(i+1,i+2):
            bb=bb+kk[j]
            if int(bb)<27 and int (bb)>0: aa=aa+1
            elif int(bb)==0: aa=aa-1
            else: break
if aa!=1: dd=aa%2
print(aa+dd+1)
            
