"""
REST

HTTP 메소드 : 클라이언트가 수행하고 싶은 처리를 서버에 전달
GET : 데이터 참조
POST : 데이터 신규 등록
PUT : 데이터 수정
DELETE : 데이터 삭제
"""

import urllib.request
import json

payload = {'key1': 'value1', 'key2': 'value2'}

# get 방식
# url = 'http://httpbin.org/get' + '?' + urllib.parse.urlencode(payload)
#
# with urllib.request.urlopen(url) as f:
#     r = json.loads(f.read().decode('utf-8'))
#     print(type(r))

# POST  방식
payload = json.dumps(payload).encode('utf-8')
req = urllib.request.Request('http://httpbin.org/post', data=payload, method='POST')
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))

# PUT  방식
print("################# PUT ######################")
req = urllib.request.Request('http://httpbin.org/put', data=payload, method='PUT')
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))

# DELETE
print("################# DELETE ######################")
req = urllib.request.Request('http://httpbin.org/delete', data=payload, method='DELETE')
with urllib.request.urlopen(req) as f:
    print(json.loads(f.read().decode('utf-8')))