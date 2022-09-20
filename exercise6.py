print('세 자리의 암스트롱 수:')
num=[]
for i in range(100,1000):

    a=i//100

    b=i%100//10

    c=i%10

    if a**3+b**3+c**3==i:
     num.append(i)
print(num)