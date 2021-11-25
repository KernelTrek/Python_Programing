with open('test.txt', 'r') as f:
    # 현재 위치를 읽어옴
    print(f.tell())
    print(f.read(1))
    print(f.tell())

    # seek 를 이용해 위치를 변경할 수 있음.
    f.seek(5)
    print(f.tell())

    f.seek(5)
    print(f.read(1))

    f.seek(10)
    print(f.read(1))