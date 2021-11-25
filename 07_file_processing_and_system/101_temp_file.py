import tempfile

# 임시 파일을 생성하고 바로 지워버림
with tempfile.TemporaryFile(mode='w+') as t:
    t.write('hello')
    t.seek(0)
    print(t.read())

# 임시파일을 삭제하지 않길 원하는 경우.
with tempfile.TemporaryFile(delete=False) as t:
    print(t.name)
    with open(t.name, 'w+') as f:
        f.write('test')
        f.seek(0)
        print(f.read())

with tempfile.TemporaryDirectory() as td:
    print(td)