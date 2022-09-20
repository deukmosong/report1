a=int(input('숫자를 입력하세요:'))
b=1
for i in range(2,a):
    if a%i==0:
        b=0
if b==1:
    print(a,'는 소수입니다')
else :
    print(a,'는 소수가 아닙니다')

        
