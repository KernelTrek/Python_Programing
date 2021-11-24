# else 문의 경우 정상 종료 될때만 실행 된다.

for fruit in ['aaple', 'banana', 'orange']:
    if fruit =='banana':
        print('stop eating')
        break
    print(fruit)
else:
    print('I ate all!')


