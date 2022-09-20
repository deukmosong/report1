n=int(input('n을 입력하시오:'))
for i in range(1,n*n+1):
    if i%n==0 :
        print(i)
    else :
        print(i,end=' ')
    