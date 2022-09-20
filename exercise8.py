print('맛나 식당에 오신 것을 환영합니다.메뉴는 다음과 같습니다.')
print('-삼겹구이(입력 s)')
print('-오삼불고기(입력 o)')
print('-된장찌개(입력 d)')
menu=input('메뉴를 선택하세요(알파벳 s,o,d 입력):')
b=0
while b==0:
    if menu=='s':
        b=1
        print('삼겹구이를 선택하셨습니다.')
    elif menu=='o':   
        b=1
        print('오삼불고기를 선택하셨습니다')
    elif menu=='d':
        b=1
        print('된장찌개를 입력하셨습니다.')
    else :
        menu=input('메뉴를 다시 입력하세요:')

