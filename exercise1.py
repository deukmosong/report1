a,b,c=input('세 정수를 입력하시오:').split()
a,b,c,=int(a),int(b),int(c)
if a>b and b>c :
    print(c,b,a)
if a>b and c>a :
     print(b,a,c)
if c>b and b>a :
    print(a,b,c)
if a>b and c>b :
    print(b,c,a)
if b>a and a>c :
 print(c,a,b)
 if b>a and c>a:
    print(a,c,b)