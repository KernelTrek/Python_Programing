s = """\
AAA
BBB
CCC
DDD
"""

# 해결 방법 w+
with open('test.txt', 'w+') as f:
    f.write(s)
    # 쓰기모드로 했을경우 읽기가 되지 않음
    f.seek(0)
    print(f.read())

# 해결 방법 w+
with open('test.txt', 'r+') as f:
    print(f.read())
    f.seek(0)
    f.write(s)
    # 쓰기모드로 했을경우 읽기가 되지 않음


#
# with open('test.txt', 'w') as f:
#     f.write(s)
#     # 쓰기모드로 했을경우 읽기가 되지 않음
#     #print(f.read())
#
# with open('test.txt', 'r') as f:
#     print(f.read())