M=int(input())
K=0
while(M>0):
  C=M%10
  K=K*10+C
  M=M//10
print(K)
  
