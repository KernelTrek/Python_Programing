r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3)) # 3은 몇번째 인덱스에 있는가 ?
print(r.index(3, 4)) #특정 위치 뒤에서 부터 검색

print(r.count(3))

if 5 in r:
    print('exist')

if 100 not in r:
    print('not exist')

r.sort()
print(r)

r.reverse() # r.sort(revers=True)
print(r)

s = 'My name is Mike.'
to_split = s.split(' ')
print(to_split)

x = ' '.join(to_split)
print(x)

# help 보는 방법
help(list)

