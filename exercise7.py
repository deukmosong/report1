a=int(input('1에서 9까지의 수를 입력하세요:'))
b=0
while b==0:
    if a<=10:
        b=1
        for i in range(1,10):
           print(a,'*',i,'=',a*i)
    else :
        a=int(input('1에서 9까지의 수를 다시 입력하세요:'))