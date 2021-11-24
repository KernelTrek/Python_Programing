l = [1, 2, 3]
i = 5

try:
    print(l[i])
except:
    print("Don't worry")

try:
    print(l[i])
except IndexError as ex:
    print("Don't worry: {}".format(ex))

print("last")

del l
try:
    print(l[i])
except IndexError as ex:
    print("Don't worry: {}".format(ex))
# 아래는 좋은 패턴은 아님 ( 에러가 나지 않게 하는 것 보다.. 정확한 에러를 잡는게 더 중요함 )
except Exception as ex:
    print('other:{}'.format(ex))
# 에러없이 정상 종료되면 아래의 메세지가 출력이 된다.
else:
    print('done')
# 실패하더라도 반드시 아래줄은 실행된다.
finally:
    print('clean up')