s = """\
AAA
BBB
CCC
DDD
"""
# with open('test.txt', 'w') as f:
#     f.write(s)

with open('test.txt', 'r') as f:
    # 전체 읽어옴
    #print(f.read())
    # 한줄씩 읽기
    # while True:
    #     line = f.readline()
    #     print(line, end='')
    #     if not line:
    #         break
    # chunk 단위로도 읽을수 있음. [네트워크에서 패킷 단위로 읽을때 주로 사용]
    while True:
        chunk = 2
        line = f.read(chunk)
        print(line)
        if not line:
            break