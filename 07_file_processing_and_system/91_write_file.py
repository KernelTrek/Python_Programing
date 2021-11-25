f = open('text.txt', 'w')
f.write('Test\n')

# print 는 잘 사용하지 않음
#print('I am print', file=f)
#print('My', 'Name','I am print', file=f)
f.close()