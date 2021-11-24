num_list = [i for i in range(10)]

for i in num_list:
    print(i)

for i in range(10):
    print(i)

# range([시작번호] , [종료번호], [증가 횟수])
for i in range(2, 10, 3):
    print(i)

# _ 를 함께 쓰는 경우 변수를 사용하지 않는 경우임.
for _ in range(10):
    print('hello')