import sqlite3

# 파일이 없으면 생성됨
#conn = sqlite3.connect('test_sqlite.db')

# test 를 할때 사용하는 것 [임시 db 저장 되지 않는 DB 임]
conn = sqlite3.connect(':memory:')

# sqlite 를 조작하기 위한 cursor
curs = conn.cursor()


curs.execute(
    'CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)')
conn.commit()

curs.execute(
    'INSERT INTO persons(name) values("Mike")'
)
conn.commit()

curs.execute('SELECT * FROM persons')
print(curs.fetchall())

curs.execute(
    'INSERT INTO persons(name) values("Nancy")'
)
curs.execute(
    'INSERT INTO persons(name) values("Jun")'
)
conn.commit()

curs.execute('UPDATE persons set name ="Michel" where name = "Mike"')
conn.commit()

curs.execute('DELETE FROM persons WHERE name = "Michel"')
conn.commit()


curs.execute('SELECT * FROM persons')
print(curs.fetchall())

# db 종료
conn.close()
