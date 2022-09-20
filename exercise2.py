x,y=input('점의 좌표 x,y를 입력하시오:').split()
x,y=int(x),int(y)
if x>0 and y>0 :
    pirnt('1사분면에 있음')
if x>0 and y<0 :
    print('4사분면에 있음')
if x<0 and y<0 :
    print('3사분면에 있음')
if x<0 and y>0:
    print('2사분면에 있음')